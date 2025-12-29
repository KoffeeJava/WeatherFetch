# This is used for making everything into an easy exacutible!

pyinstaller -F main.py -n wfetch
echo "wfetch built!"
pyinstaller -F WM-setup.py -n WM-setup
echo "WM-setup built!"