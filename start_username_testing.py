from instabot import NoAccountBot, load_config
import time, sys

cfg = load_config.load_json()
path = cfg['general'].get('driver_path')

print("--- Start testing usernames ---")
print("stop it by pressing CTRL+C")
print("")
print("Log:")

bot = NoAccountBot(path=path)
time.sleep(30)


""" names = open("names.txt", "r")
available_names = open("available.txt", "a")

for name in names:
    bot.open_profile(name)
    if bot.check_existenz():
        print("[ ✘ ] " + name)
    else:
        print("[ ✓ ] " + name)
        available_names.write(name)

available_names.close()
names.close() """

bot.edit_profile()

names = open("available.txt", "r")
free_names = open("free_names.txt", "a")

for name in names:
    sleep(1)
    if bot.change_username(name):
        print("[ ✓ ] " + name)
        free_names.write(name)
    else:
        print("[ ✘ ] " + name)

names.close()
free_names.close()

time.sleep(120)


bot.close()