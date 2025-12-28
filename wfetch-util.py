import os
import sys
from dialog import Dialog
import shutil

d = Dialog(dialog="dialog")

try:
    arg = sys.argv[1]
except:
    arg = ""

if arg == "":
    d.set_background_title("Wfetch Installer")

    if os.geteuid() != 0:
        d.msgbox("You are not in root! Please enter root to install Wfetch.")
        os.system("clear")
        sys.exit(1)

    d.msgbox("Hello! This is the better installer for Wfetch!")
    code, path = d.dselect("/usr/bin", title="Please chose an install location")

    if d.yesno("Do you want to continue installing?") == d.OK:

        if code == d.OK:
           shutil.copyfile("data/wfetch", os.path.expanduser(f"{path}/wfetch"))
           os.system("chmod +x /usr/bin/wfetch")
        else:
            os.system("clear")
            print("Aborted install")
            sys.exit(1)

        d.msgbox("wfetch is now installed! Please run ./install -s to setup.")
    
    else:
        os.system("clear")
        print("aborted install")
        sys.exit(0)

if arg == "-u" or arg == "--uninstall":
    os.system("rm /usr/bin/wfetch")
    os.system("rm -rf $HOME/.local/share/Wfetch")

if arg == "-s" or arg == "--setup":
        d.set_background_title("Wfetch Setup")

        code, string = d.inputbox("Please enter a Weather Api Key.\nYou can get one at https://www.weatherapi.com/")

        if code == d.OK:
            os.makedirs(os.path.expanduser("~/.local/share/Wfetch"))

            api = string

            code, string = d.inputbox("Now please enter the city you live in.")

            if code == d.OK:
                city = string

                with open(os.path.expanduser("~/.local/share/Wfetch/config.toml"), "w") as f:
                    f.write(f"api = \"{api}\"")
                    f.write(f"\ncity = \"{city}\"")
            
                code, tag = d.menu("Please select which unit you want to use. NOTE: You can customise how everything is shown!",
                       choices=[("(1)", "Customary"),
                                ("(2)", "Metric"),
                                ("(3)", "Both")])
            
                if tag == "(1)":
                    shutil.copyfile("data/cust.toml", os.path.expanduser("~/.local/share/Wfetch/disp.toml"))
                elif tag == "(2)":
                    shutil.copyfile("data/met.toml", os.path.expanduser("~/.local/share/Wfetch/disp.toml"))
                elif tag == "(3)":
                    shutil.copyfile("data/both.toml", os.path.expanduser("~/.local/share/Wfetch/disp.toml"))

                d.msgbox("Setup has finnished! If you installed wfetch to /usr/bin you can run wfetch just by typing wfetch into your terminal.")
                sys.exit(0)

        
            else:
                os.system("clear")
                print("You have exited the setup! Don't worry, You can start it again by running \"./install -s\"")
                sys.exit(1)