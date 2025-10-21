import os
import sys
import shutil
from colorist import ColorHex

wf_orange = ColorHex("#ffc83d")
error_red = ColorHex("#ff0000")

if os.geteuid() != 0:
        print(f"\033[1m{error_red}You must be in root to Install Wfetch!{error_red.OFF}")
        sys.exit(1)

shutil.copyfile("wfetch", os.path.expanduser("/usr/bin/wfetch"))
shutil.copyfile("disp.toml", os.path.expanduser("/home/koffeejava/.local/share/Wfetch/disp.toml"))

os.system("chmod +x /usr/bin/wfetch")

print(f"\033[1m{wf_orange}Install finished. Enjoy!{wf_orange.OFF}")    