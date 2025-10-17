# Note: This script does not work when not running in the exicutible (i'm bad at spelling!)

import os
import sys
import shutil
from colorist import ColorHex

wf_orange = ColorHex("#ffc83d")
error_red = ColorHex("#ff0000")


if os.geteuid() != 0:
        print(f"\033[1m{error_red}You must be in root to remove Wfetch!{error_red.OFF}")
        sys.exit(1)
os.system("rm /usr/bin/wfetch")
os.system("rm -rf /home/koffeejava/.local/share/Wfetch/")
print(f"\033[1m{wf_orange}Uninstallation finished!{wf_orange.OFF}")