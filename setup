#!/bin/bash
### Yukki Music Bot Installer

pprint (){
	cred='\033[0;31m'
	cgreen='\033[0;32m'
	cyellow='\033[0;33m'
	cblue='\033[0;34m'
	cpurple='\033[0;35m'
	eval "export color='$cpurple'"
	[ ! -z $2 ] && eval "export color=\"\$$2\""
    printf "$color $1"
}

color_reset(){ printf '\033[0;37m';}

yesnoprompt(){
	old_stty_cfg=$(stty -g)
	stty raw -echo ; answer=$(head -c 1)
	stty $old_stty_cfg
	echo "$answer" | grep -iq "^y"
}

update() {
	pprint "\n\nUpdating package list.. "
	sudo apt update 2>&1 | grep "can be upgraded" &>/dev/null
	if [ $? -eq 0 ]; then
		pprint "UPDATE AVAILABLE" "cgreen"
		pprint "\n\nDo you want to automatically upgrade (y/n)?"
		if yesnoprompt; then
			pprint "\n\nUpgrading packages.. "
			sudo apt upgrade -y &>/dev/null &&
			pprint "DONE!\n\n" "cgreen" || (pprint "FAIL.\n\n" "cred"; exit 1)
		else
			echo
		fi
	else
		pprint "ALREADY UP TO DATE\n\n" "cgreen"
	fi
}

packages(){
	if ! command -v pip &>/dev/null; then
		pprint "Couldn't found pip, installing now.. "
		sudo apt install python3-pip -y 2>pypilog.txt 1>/dev/null &&
		pprint "SUCCESS.\n\n" "cgreen" || (pprint "FAIL.\n\n" "cred"; exit 1)
	fi

	if ! command -v ffmpeg &>/dev/null; then
		pprint "Couldn't found ffmpeg, installing now.. "
		if sudo apt install ffmpeg -y &>/dev/null;then
			pprint "SUCCESS.\n\n" "cgreen"
		else
			pprint "FAIL.\n\n" "cred"
			pprint "You need to install ffmpeg manually in order to use YukkiMusicBot, exiting..\n" "cblue"
			exit 1
		fi
	fi

	# Check ffmpeg version and warn user if necessary.
	fv=$(grep -Po 'version (3.*?) ' <<< $(ffmpeg -version)) &&
	pprint "Playing live streams not going to work since you have ffmpeg $fv, live streams are supported by version 4+.\n" "cblue"
}


node(){
	command -v npm &>/dev/null && return
	pprint "Installing Nodejs and Npm..  "
	curl -fssL https://deb.nodesource.com/setup_17.x | sudo -E bash - &>nodelog.txt &&
	sudo apt install nodejs -y &>>nodelog.txt &&
	sudo npm i -g npm &>>nodelog.txt &&
	pprint "SUCCESS!\n" "cgreen" || (pprint "FAIL.\n" "cred"; exit 1)
}


repo(){
	# Get git repo if the installer is runned standalone
	[[ ! "YukkiMusicBot" == $(basename -s .git `git config --get remote.origin.url`) ]] &&
	git clone https://github.com/notreallyshikhar/YukkiMusicBot &&  cd YukkiMusicBot
}


installation(){
	pprint "\n\nUpgrading pip and installing dependency packages.. "
	pip3 install -U pip &>>pypilog.txt &&
	pip3 install -U -r requirements.txt &>>pypilog.txt &&
	pprint "DONE.\n" "cgreen" && return
	pprint "FAIL.\n" "cred"
	exit 1
}

clear
pprint "Welcome to Yukki Music Bot Setup Installer\n\n"
pprint "If you see any error during Installation Process, Please refer to these files for logs: "
pprint "\nFor node js errors , Checkout nodelog.txt"
pprint "\nFor pypi packages errors , Checkout pypilog.txt"
sleep 2
pprint "\n\nScript needs sudo privileges in order to update & install packages.\n"
sudo test

update
packages
node
repo
installation
pprint "\n\n\n\n\nYukki Music Bot Installation Completed!" "cgreen"
sleep 4
clear

pprint "\nEnter Your Values Below\n\n\n"
pprint "API ID: "; color_reset; read api_id
pprint "\nAPI HASH: "; color_reset; read api_hash
pprint "\nBOT TOKEN: "; color_reset; read bot_token
pprint "\nMONGO DB URI: "; color_reset; read mongo_db
pprint "\nLOG GROUP ID: "; color_reset; read logger
pprint "\nPYROGRAM STRING SESSION OF ASSISTANT ACCOUNT: "; color_reset; read string_session
pprint "\nMUSIC BOT NAME: "; color_reset; read mbt
pprint "\nOwner Id:"; color_reset; read ownid

pprint "\n\nProcessing your vars, Wait a while!" "cgreen"

if [ -f .env ]; then
	rm .env
fi

echo """API_ID = $api_id
API_HASH = $api_hash
BOT_TOKEN = $bot_token
MONGO_DB_URI = $mongo_db
LOG_GROUP_ID = $logger
MUSIC_BOT_NAME = $mbt
STRING_SESSION = $string_session
OWNER_ID = $ownid""" > .env
clear
pprint "\n\n\nYour Vars have been saved Successfully!, Thanks for using Yukki Installer, now you can proceed by starting the bot with bash start!"
pprint "\n\n\nWant more vars?"
pprint "\nCheckout config.py and readme.md inside config folder for addtional vars. You can change all images , Thumbs, mode and everything from vars. Have a look towards them\n\n"
