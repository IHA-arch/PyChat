#!/bin/bash
root() {
user=`whoami`
if [[ $user != 'root' ]]; then
	echo "Please run as root\n"
	exit
fi
}

printf "installing pyautogui....\n"
pip install PyAutoGUI

printf "installing random2....\n"
pip install random2


access() {
cp pychat_IHA.py /usr/share
cp pychat /usr/local/bin

chmod +x /usr/local/bin/pychat

printf "\n\ntype 'pychat' anywhere on the terminal\n"
}

root
access

