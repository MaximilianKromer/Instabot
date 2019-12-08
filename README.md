# Instabot

a python Instragram-Bot with Chrome and Selenium


# Setup

All you need is [Python](https://www.python.org/downloads/), [Chrome](https://www.google.com/intl/de_de/chrome/) and [Chromedriver](https://chromedriver.chromium.org/)

## Chromedriver

Check your Chrome version and download the Chromedriver for your version.
Then move that file to your instabot directory.

## Python Setup

Open a console in your instabot directory and type the following command:

    pip install -r requirements.txt

if that doesn't work try:

    pip3 install -r requirements.txt

## Config

Rename 'example.config.json' to 'config.json' and open it with an editor

### general

Insert the path to the chromedriver

    "driver_path": "<your_path>/instabot/chromedriver",

### single_bot

Insert your login credentials to the config.json


# Usage

List of all functions and how to use them.

Usage:

    python start.py <single|multi> <follow|like|auto_accept> [username]

or

    python3 start.py <single|multi> <follow|like|auto_accept> [username]


## Single

Do the operation with only one account

### follow

Type in the name of the user to follow

	start.py single follow [username]

### auto_accept

Accept all new follow requests.

    start.py single auto_accept

> Press "CTRL + C" to stop it


# Known Issues
 
Multiple accounts aren't supported yet.
