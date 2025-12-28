# This is used for making everything into an easy exacutible!

pyinstaller -F main.py -n wfetch
echo "wfetch built!"
pyinstaller -F wfetch-util.py -n wfetch-util