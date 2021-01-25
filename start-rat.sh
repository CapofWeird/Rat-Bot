#!/bin/bash -x
# Set paths here.
RATDIR="/home/hatofnormal"
ENVFOLDER="env"
URL="https://github.com/CapofWeird/Rat-Bot.git"
# Update the rat
cd $RATDIR
git pull $URL
# Starts up the rat
source $RATDIR/$ENVFOLDER/bin/activate
pip3 install -r requirements.txt
python3.6 $RATDIR/rat_bot.py
