#!/bin/bash -x
# Set paths here.
RATDIR="/home/hatofnormal"
ENVFOLDER="env"
URL="https://github.com/CapofWeird/Rat-Bot.git"
# Update the rat
git pull $URL
# Starts up the rat
source $RATDIR/$ENVFOLDER/bin/activate
python3.6 $RATDIR/rat_bot.py