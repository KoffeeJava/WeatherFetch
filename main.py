# Main file of wfetch. You can kinda read it.

import math
import os
import shutil
import sys

import requests
from colorist import ColorHex

import chk_id

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

if not os.path.exists(os.path.expanduser("~/.local/share/Wfetch")):
    os.makedirs(os.path.expanduser("~/.local/share/Wfetch"))

if arg == "" or arg == "--debug":
    print(f"\033[1m{wf_orange}WeatherFetch KoffeeWare 2025{wf_orange.OFF}")
    try:
        with open(os.path.expanduser("~/.local/share/Wfetch/config.cfg")) as f:
            content = f.readlines()
            api_key = content[0].rstrip()
            city = content[1].rstrip()
            unit = content[2]

            if arg == "--debug":
                print(f"\033[1m{debug_orange}Read API key as: {api_key}{debug_orange.OFF}")
                print(f"\033[1m{debug_orange}Read city as: {city}{debug_orange.OFF}")
                print(
                    f"\033[1m{debug_orange}Read unit of measure as: {unit} (c for customary and m for metric){debug_orange.OFF}")
    except:
        print(f"\033[1m{error_red}the config file was not found! Please run wfetch -s")
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

        chk_id.id_to_icon(id)

        if unit == "c":
            if temp > 85:
                print(f"Live Temperature: \033[1m{hot_red}{temp}°F{hot_red.OFF}")
            elif temp in range(70, 84):
                print(f"Live Temperature: \033[1m{warm_orange}{temp}°F{warm_orange.OFF}")
            elif temp < 70:
                print(f"Live Temperature: \033[1m{cold_blue}{temp}°F{cold_blue.OFF}")

            if fctemp > 85:
                print(f"Feels like: \033[1m{hot_red}{fctemp}°F{hot_red.OFF}")
            elif fctemp in range(70, 84):
                print(f"Feels like: \033[1m{warm_orange}{fctemp}°F{warm_orange.OFF}")
            elif fctemp < 70:
                print(f"Feels like: \033[1m{cold_blue}{fctemp}°F{cold_blue.OFF}")
        elif unit == "m":
            if tempm > 29:
                print(f"Live Temperature: \033[1m{hot_red}{tempm}°C{hot_red.OFF}")
            elif tempm in range(21, 28):
                print(f"Live Temperature: \033[1m{warm_orange}{tempm}°C{warm_orange.OFF}")
            elif tempm < 21:
                print(f"Live Temperature: \033[1m{cold_blue}{tempm}°C{cold_blue.OFF}")

            if fctemp > 29:
                print(f"Feels like: \033[1m{hot_red}{fctemp}°C{hot_red.OFF}")
            elif fctemp in range(21, 28):
                print(f"Feels like: \033[1m{warm_orange}{fctemp}°C{warm_orange.OFF}")
            elif fctemp < 21:
                print(f"Feels like: \033[1m{cold_blue}{fctemp}°C{cold_blue.OFF}")

        if unit == "c":
            if cwind in range(1, 12):
                print(f"Wind Speed: \033[1m{cold_blue}{cwind} Mph")
            elif cwind in range(13, 25):
                print(f"Wind Speed: \033[1m{warm_orange}{cwind} Mph{warm_orange.OFF}")
            elif cwind in range(26, 73):
                print(f"Wind Speed: \033[1m{hot_red}{cwind} Mph{hot_red.OFF}")
        elif unit == "m":
            print(f"Wind Speed: {mwind} Km/h")

        print(f"Humidity: {humidity}%")
        print(f"Weather Description: \033[1m{wf_orange}{desc}{wf_orange.OFF}")
    else:
        print('Error fetching weather data!')
if arg == "--help" or arg == "-h":
    print(f"\033[1m{wf_orange}Wfetch 2025 KoffeeWare{wf_orange.OFF}")
    print("Usage: Wfetch [options]\n")
    print("-h, --help           This help page.")
    print("-s, --setup           Setup Wfetch.")
    print("-v, --version           Show version of Wfetch.")
    print("--debug      Debug features. Good for seeing of config file is being read correctly.")
    print("--show-icons        shows all icons. I use this for editing icons.")

if arg == "-s" or arg == "--setup":
    print("Welcome to the WeatherFetch Setup.")
    api_key = input("Please enter your API key from openweathermap.org: ")
    city = input("Please enter your city name: ")
    unit = input("Customary or metric? (c/m): ")

    with open(os.path.expanduser("~/.local/share/Wfetch/config.cfg"), "w") as f:
        f.write(api_key)
        f.write(f"\n{city}")
        f.write(f"\n{unit}")

if arg == "--show-icons":
    chk_id.all()
    print("finished")

if arg == "-v" or arg == "--version":
    print("v2.0 Full Release")
