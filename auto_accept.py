from instabot import SingleAccountBot, load_config
import time, sys


cfg = load_config.load_json()
path = cfg['general'].get('driver_path')
username = cfg['single_bot'].get('username')
password = cfg['single_bot'].get('password')
timeout = cfg['general'].get('auto_accept').get('timeout')
limit = cfg['general'].get('auto_accept').get('limit')

print("--- Auto accept all follow requests ---")
print("stop it by pressing CTRL+C")
print("")
print("Log:")

bot = SingleAccountBot(username=username, password=password, path=path)
time.sleep(2)
while True:
    follower = bot.get_followers()
    print("Follower: " + str(follower) + "/" + str(limit))
    while follower < limit:
        bot.open_followlist()
        time.sleep(5)
        bot.accept_one_follow()
        follower = follower + 1
    
    time.sleep(timeout)