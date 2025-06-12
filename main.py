import math
import os
import readline
import shutil
import sys

import requests
from colorist import ColorHex

import chk_id

try:
    arg = sys.argv[1]
except:
    arg = ""

wf_orange = ColorHex("#ffc83d")
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
        print(f"{error_red}the config file was not found! Please reinstall Wfetch")

    fetch_url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}"

    if arg == "--debug":
        print(f"\033[1m{debug_orange}Full fetch url: {fetch_url}{debug_orange.OFF}")

    response = requests.get(fetch_url)

    if response.status_code == 200:
        data = response.json()

        if arg == "--debug":
            print(f"\033[1m{debug_orange}Fetched: {data}{debug_orange.OFF}")

        tem = data['main']['temp']
        ftem = data['main']['feels_like']
        ftemp = math.floor((ftem - 273.15) * 9 / 5 + 32)
        ftempm = math.floor((ftemp - 32) / 1.8)
        temp = math.floor((tem - 273.15) * 9 / 5 + 32)
        tempm = math.floor((temp - 32) / 1.8)
        desc = data['weather'][0]['description']
        press = data['main']['pressure']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        id = data['weather'][0]['id']

        chk_id.id_to_icon(id)

        if unit == "c":
            if temp > 85:
                print(f"Live Temperature: \033[1m{hot_red}{temp}°F{hot_red.OFF}")
            elif temp in range(70, 84):
                print(f"Live Temperature: \033[1m{warm_orange}{temp}°F{warm_orange.OFF}")
            elif temp < 70:
                print(f"Live Temperature: \033[1m{cold_blue}{temp}°F{cold_blue.OFF}")

            if ftemp > 85:
                print(f"Feels like: \033[1m{hot_red}{ftemp}°F{hot_red.OFF}")
            elif ftemp in range(70, 84):
                print(f"Feels like: \033[1m{warm_orange}{ftemp}°F{warm_orange.OFF}")
            elif ftemp < 70:
                print(f"Feels like: \033[1m{cold_blue}{ftemp}°F{cold_blue.OFF}")
        elif unit == "m":
            if tempm > 29:
                print(f"Live Temperature: \033[1m{hot_red}{tempm}°C{hot_red.OFF}")
            elif tempm in range(21, 28):
                print(f"Live Temperature: \033[1m{warm_orange}{tempm}°C{warm_orange.OFF}")
            elif tempm < 21:
                print(f"Live Temperature: \033[1m{cold_blue}{tempm}°C{cold_blue.OFF}")

            if ftempm > 29:
                print(f"Feels like: \033[1m{hot_red}{ftempm}°C{hot_red.OFF}")
            elif ftempm in range(21, 28):
                print(f"Feels like: \033[1m{warm_orange}{ftempm}°C{warm_orange.OFF}")
            elif ftempm < 21:
                print(f"Feels like: \033[1m{cold_blue}{ftempm}°C{cold_blue.OFF}")

        # print(f"Air Pressure: {press}") May remove soon!
        if unit == "c":
            if math.floor(wind / 1.609344) in range(1, 12):
                print(f"Wind Speed: \033[1m{cold_blue}{math.floor(wind / 1.609344)} Mph{cold_blue.OFF}")
            elif math.floor(wind / 1.609344) in range(13, 25):
                print(f"Wind Speed: \033[1m{warm_orange}{math.floor(wind / 1.609344)} Mph{warm_orange.OFF}")
            elif math.floor(wind / 1.609344) in range(26, 73):
                print(f"Wind Speed: \033[1m{hot_red}{math.floor(wind / 1.609344)} Mph{hot_red.OFF}")
        elif unit == "m":
            print(f"Wind Speed: {wind} Km/h")

        print(f"Humidity: {humidity}%")
        print(f"Weather Description: \033[1m{wf_orange}{desc}{wf_orange.OFF}")
    else:
        print('Error fetching weather data')
if arg == "--help" or arg == "-h":
    print(f"\033[1m{wf_orange}Wfetch 2025 KoffeeWare{wf_orange.OFF}")
    print("Usage: Wfetch [options]\n")
    print("-h           This help page.")
    print("-s           Setup Wfetch.")
    print("-i           Install Wfetch to usr/bin/")
    print("-u           Uninstall Wfetch. Required to update Wfetch!")
    print("-v           Show version of Wfetch.")
    print("--debug      Debug features. Good for seeing of config file is being read correctly.")

if arg == "-s":
    print("Welcome to the WeatherFetch Setup.")
    api_key = input("Please enter your API key from openweathermap.org: ")
    city = input("Please enter your city name: ")
    unit = input("Customary or metric? (c/m): ")

    with open(os.path.expanduser("~/.local/share/Wfetch/config.cfg"), "w") as f:
        f.write(api_key)
        f.write(f"\n{city}")
        f.write(f"\n{unit}")

if arg == "-i":

    if os.geteuid() != 0:
        print(f"\033[1m{error_red}You must be in root to Install Wfetch!{error_red.OFF}")
        sys.exit(1)
    shutil.copyfile("Wfetch", os.path.expanduser("/usr/bin/Wfetch"))

    os.system("chmod +x /usr/bin/Wfetch")

    print(f"{wf_orange}Install finished. Enjoy!{wf_orange.OFF}")

if arg == "-u":
    if os.geteuid() != 0:
        print(f"\033[1m{error_red}You must be in root to Install Wfetch!{error_red.OFF}")
        sys.exit(1)
    os.system("rm /usr/bin/Wfetch")
    os.system("rmdir ~/.local/share/Wfetch/")
    print(
        f"\033[1m{wf_orange}Uninstallation finnished! If updating run sudo ./Wfetch -i ON THE NEW FILE{wf_orange.OFF}")

if arg == "-v":
    print("v1.1 Full Release")
