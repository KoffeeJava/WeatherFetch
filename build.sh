# This is used for making everything into an easy exacutible!

cd ~/Desktop/WeatherFetch
pyinstaller -F main.py -n wfetch
echo "wfetch built! (I hope so.)"
pyinstaller -F uninstall.py -n uninstall
echo "uninstall script built! (I hope so.)"
pyinstaller -F install.py -n install
echo "Install script built! (I hope so.)"
echo "Finished!"