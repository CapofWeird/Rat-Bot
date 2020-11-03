#!/bin/bash -x
# Set paths here.
RATDIR="/home/hatofnormal"
ENVFOLDER="env"
# Starts up the rat
source $RATDIR/$ENVFOLDER/bin/activate
python3.6 $RATDIR/rat_bot.py