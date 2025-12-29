# Main file of wfetch. You can kinda read it.

import math
import os
import shutil
import sys
import toml
import requests
from colorist import ColorHex
import chk_id
from datetime import datetime

try:
    arg = sys.argv[1]
except:
    arg = ""

wf_orange = ColorHex("#ee8b00")
error_red = ColorHex("#ff0000")
hot_red = ColorHex("#ff3d3d")
warm_orange = ColorHex("#ffc83d")
cold_blue = ColorHex("#3f42ff")
debug_orange = ColorHex("#ffbc21")

if arg == "" or arg == "--debug":
    print(f"\033[1m{wf_orange}WeatherFetch KoffeeJava 2025{wf_orange.OFF}")
    try:
        with open(os.path.expanduser("config.toml")) as f:
            content = toml.load(f)
            api_key = content['api']
            city = content['city']

            if arg == "--debug":
                print(f"\033[1m{debug_orange}Read API key as: {api_key}{debug_orange.OFF}")
                print(f"\033[1m{debug_orange}Read city as: {city}{debug_orange.OFF}")
                print(f"\033[1m{debug_orange}Current Time: {int(datetime.now().strftime("%H%M"))}{debug_orange.OFF}")

    except:
        print(f"\033[1m{error_red}The config file was not found! Please run the wfetch-util setup.\033[0m")
        sys.exit(1)

    try:
            with open(os.path.expanduser('disp.toml'), 'r') as f:
                order = toml.load(f)
    except:
            print(f"\033[1m{hot_red}Your Config file for displaying information is missing!\nCreate one by copy one of the examples into the directory wfetch is in.{hot_red.OFF}\033[0m")
            sys.exit(1)

    fetch_url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"

    if arg == "--debug":
        print(f"\033[1m{debug_orange}Full fetch url: {fetch_url}{debug_orange.OFF}")

    response = requests.get(fetch_url)

    if response.status_code == 200:
        data = response.json()

        if arg == "--debug":
            print(f"\033[1m{debug_orange}Fetched: {data}{debug_orange.OFF}")

        fftemp = data['current']['feelslike_f']
        fctemp = data['current']['feelslike_c']
        temp = data['current']['temp_f']
        tempm = data['current']['temp_c']
        desc = data['current']['condition']['text']
        press = data['current']['pressure_in']
        cwind = data['current']['wind_mph']
        mwind = data['current']['wind_kph']
        humidity = data['current']['humidity']
        id = data['current']['condition']['code']

        if temp > 85:
            temp_format = f"\033[1m{hot_red}{temp }{hot_red.OFF}"
        elif temp in range(70, 84):
            temp_format = f"\033[1m{warm_orange}{temp}{warm_orange.OFF}"
        elif temp < 70:
            temp_format = f"\033[1m{cold_blue}{temp}{cold_blue.OFF}"

        if fftemp > 85:
            fftemp_format = f"\033[1m{hot_red}{fftemp}{hot_red.OFF}"
        elif temp in range(70, 84):
            fftemp_format = f"\033[1m{warm_orange}{fftemp}{warm_orange.OFF}"
        elif temp < 70:
            fftemp_format = f"\033[1m{cold_blue}{fftemp}{cold_blue.OFF}"

        if tempm > 29:
                tempm_format = f"\033[1m{hot_red}{tempm}{hot_red.OFF}"
        elif tempm in range(21, 28):
                tempm_format = f"\033[1m{warm_orange}{tempm}{warm_orange.OFF}"
        elif tempm < 21:
                tempm_format = f"\033[1m{cold_blue}{tempm}{cold_blue.OFF}"
        
        if fctemp > 29:
                fctemp_format = f"\033[1m{hot_red}{fctemp}{hot_red.OFF}"
        elif fctemp in range(21, 28):
                fctemp_format = f"\033[1m{warm_orange}{fctemp}{warm_orange.OFF}"
        elif fctemp < 21:
                fctemp_format = f"\033[1m{cold_blue}{fctemp}{cold_blue.OFF}"

        if round(cwind) in range(1, 12):
                cwind_format = f"\033[1m{cold_blue}{cwind}{cold_blue.OFF}"
        elif round(cwind) in range(13, 25):
                cwind_format = f"\033[1m{warm_orange}{cwind}{warm_orange.OFF}"
        elif round(cwind) in range(26, 73):
                cwind_format = f"\033[1m{hot_red}{cwind}{hot_red.OFF}"

        if round(mwind) in range(1, 19):
                mwind_format = f"\033[1m{cold_blue}{mwind}{cold_blue.OFF}"
        elif round(mwind) in range(20, 45):
                mwind_format = f"\033[1m{warm_orange}{mwind}{warm_orange.OFF}"
        elif round(mwind) in range(46, 117):
                mwind_format = f"\033[1m{hot_red}{mwind}{hot_red.OFF}"

        desc_format = f"{desc}"

        chk_id.id_to_icon(id)

        linenum = 1

        while True:
            try:
                line = order[f'{linenum}']
            except:
                break
            line_formatted = line.format(
                feels_temp_f=fftemp_format, 
                feels_temp_c=fctemp_format, 
                temp_f=temp_format, 
                temp_c=tempm_format, 
                description=desc_format,
                bold="\033[1m".format(), # colorist gave me double lines instead of bold. WHY!!!!
                blink="\033[5m".format(),
                reset="\033[0m".format(),
                pressure=press, 
                wind_mph=cwind_format, 
                wind_kph=mwind_format,
                humidity=humidity,
                orange=wf_orange,
                orange_OFF=wf_orange.OFF,
                red=hot_red,
                red_OFF=hot_red.OFF,
                blue=cold_blue,
                blue_OFF=cold_blue.OFF)

            print(line_formatted)
            linenum += 1

    else:
        print('Error fetching weather data!')
if arg == "--help" or arg == "-h":
    print(f"\033[1m{wf_orange}Wfetch 2025 KoffeeJava{wf_orange.OFF}")
    print("Usage: Wfetch [options]\n")
    print("-h, --help           This help page.")
    print("-v, --version           Show version of Wfetch.")
    print("--debug      Debug features. Good for seeing of config file is being read correctly.")
    print("--show-icons        shows all icons. I use this for editing icons.")

if arg == "--show-icons":
    chk_id.all()
    print("finished")

if arg == "-v" or arg == "--version":
    print("v2.1 Full Release")
    toml = order['order']['1']
