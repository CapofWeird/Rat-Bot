# Rat Bot

A Discord bot that responds with rat emojis when you say the word **"rat."**

Includes words that contain **rat** and **r a t**!

## Commands
- **!oracle** - 8-ball command
  - Usage: `!oracle <whatever here>`
- **!coin** - Flip a coin

## Invite

Invite with [this link!](https://discord.com/oauth2/authorize?client_id=671793984435126277&scope=bot)

## Requirements

The current Rat Bot install uses Python 3.6, so you will need to install Python 3.6 before doing this.

It's recommended to run Rat Bot in a virtual environment. To do this, run `python3.6 -m venv env` and then activate the virtual environment.

## Installing

TL;DR (mainly for bash users):
```sh
git clone https://github.com/CapOfWeird/Rat-Bot.git
cd Rat-Bot
python3.6 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
# Change the Discord token at the bottom of rat_bot.py.
python3.6 rat_bot.py # Or, configure start-rat.sh.
```

## Installing as a Service (Linux, `systemd`)

To install Rat Bot as a service on a Linux distribution that uses `systemd`, do the following:
```sh
# It's a good idea to make a new user for this.
# This command makes a new user with a home folder, a user group matching their user, and sets their shell to bash.
sudo useradd -m -s /bin/bash -U ratbot

# You'll need to set the password of the user after this.
sudo passwd ratbot

# Now, log in as ratbot using the password you just made
su - ratbot

# Now, clone the repo
git clone https://github.com/CapOfWeird/Rat-Bot.git
cd Rat-Bot

# Set up a virtual environment (we recommend using `env` as a name as it's already gitignored.)
python3.6 -m venv env

# Go into your virtual environment.
source env/bin/activate

# Install the requirements
pip3 -m requirements.txt

# Now, edit the rat_bot.py file.
# You'll need to change the last line to contain your Discord token.
nano rat_bot.py

# Next, edit the ratbot.service file.
# You'll need to change three lines:
#   - ExecStart: This should be where the shell script is (if you've followed 
#     along exactly, the path is /home/ratbot/Rat-Bot/start-rat.sh)
#   - User: Change this to the user you created. (`ratbot` in this case.)
#   - Group: Change this to the group that your user is in 
#     (`ratbot` in this case.)
nano ratbot.service

# Now, copy the service file to your systemd directory (this varies between distributions!)
# It should be noted that you may not be able to sudo on this new account. If you can't,
# add the user to the sudoers file using `visudo`.
sudo cp ratbot.service /etc/systemd/system

# Reload daemons
sudo systemctl daemon-reload

# Edit the start-rat.sh script.
# You'll mainly need to change the `RATDIR` variable and the `ENVFOLDER` variable.
# If you've followed along with this, the variables should be:
#   - `RATDIR`: "/home/ratbot/Rat-Bot"
#   - `ENVFOLDER`: "env"
nano start-rat.sh

# You don't need to mark the script as executable, as the systemd service executes it with bash.
# Start the service, and the bot should now be running!
sudo systemctl start ratbot

# Optionally, if you want the service to start on each system boot:
sudo systemctl enable ratbot
```
