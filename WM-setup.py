import os
import sys
import shutil

print("WM-Setup KoffeeJava")

api = input("Please enter a Weather Api Key.\nYou can get one at https://www.weatherapi.com/ :")
city = input("Now please enter the city you live in:")

with open("config.toml", "w") as f:
    f.write(f"api = \"{api}\"")
    f.write(f"\ncity = \"{city}\"")
        
print("(1) Customary")
print("(2) Metric")
print("(3) Both")
disp = input("Please select which unit you want to use. NOTE: You can customise how everything is shown! :")

if disp == "(1)":
    shutil.copyfile("data/cust.toml", "disp.toml")
elif disp == "(2)":
    shutil.copyfile("data/met.toml", "disp.toml")
elif disp == "(3)":
    shutil.copyfile("data/both.toml", "disp.toml")

print("Setup has finnished! Enjoy!")



        