# WARNING!
## This is the Develoment Branch of WeatherFetch. This means It may work, or it may not work sometimes and if it works, more things can be broken.
## Use the master branch if you want to build WeatherFetch

# WeatherFetch - A weather app for your terminal.
WeatherFetch is an application that shows the live temperature, air pressure, wind speed, humidity, and weather descriptions!

# How to install and setup

Install by running the install script (`sudo ./install`) then setup wfetch via `wfetch -s`

# How to uninstall

Download or open the latest release of wftech and run `sudo ./uninstall`

# FAQ

## How do I get an Weather API key?

First, go to the (Weather API)[https://www.weatherapi.com/] website and then sign up. When finished creating an account, login then copy your api key.
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

### Wfetch
`pyinstaller -F main.py -n wfetch`

### Wfetch-util
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

