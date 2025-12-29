# WARNING!
## This is the Develoment Branch of WeatherFetch. This means It may work, or it may not work sometimes and if it works, more things can be broken.
## Use the master branch if you want to build WeatherFetch

# WeatherFetch - A weather app for your terminal.
WeatherFetch is an application that shows the live temperature, air pressure, wind speed, humidity, and weather descriptions!

# How to install and setup

## Linux
To install and setup wfetch on linux, I created a simple program called wfetch-util.

Run `./wfetch-util -i` in root and follow the wizzard to install wfetch and then setup by running `./wfetch-util -s` and follow that wizzard to.

## Windows and Macos
Installing is just downloading the lastest version as you guys only get the portable version! (Macos can put into /Applications)

You can setup by running the WM-setup program by running `./WM-setup` for both oses.

# How to uninstall

## Linux
Download or open the latest release of wftech and run `./wfetch-util -u` **(NOT IN ROOT)** and follow the wizzard.

## Windows and Macos
Just delete the directory wfetch is in :) (The pros of portable programs!)

# FAQ

## How do I get an Weather API key?

First, go to the [Weather API](https://www.weatherapi.com/) website and then sign up. When finished creating an account, login then copy your api key.
Make sure to paste that api key to setup.

## Why don't you provide an api key?
I'm lazy. (plus api call limit stuff)

# Building
To make the executable, I use pyinstaller.
All of these instructions work on Linux, Windows, and Macos.

<details>
<summary>Linux Users!</summary>
    You guys get a bash script that builds everything! Your welcome :)
</details>

## Wfetch
`pyinstaller -F main.py -n wfetch`

## Wfetch-util
` pyinstaller -F wfetch-util.py -n wfetch-util`

# To do
+ ~~Add ASCII icons~~
+ ~~Make library for description~~(I use id codes now)
+ ~~Add M-Metric units 🤢~~
+ ~~Make a Windows version~~
+ ~~Make a MacOS version~~
+ Make more people use it

# Credit
[OpenWeatherMap](https://openweathermap.org/weather-conditions): their icons were used for the ascii art.
[Weather API](www.weatherapi.com) Their api is used for this program.

