from instabot import SingleAccountBot, load_config
import time, sys


def single_follow(to_follow):
    cfg = load_config.load_json()
    path = cfg['general'].get('driver_path')
    username = cfg['single_bot'].get('username')
    password = cfg['single_bot'].get('password')


    bot = SingleAccountBot(username=username, password=password, path=path)
    time.sleep(2)
    bot.open_profile(to_follow)
    time.sleep(2)
    bot.follow()
    bot.open_ownprofile()
    time.sleep(2)
    bot.close()

try:
    if sys.argv[1] == "single":
        if sys.argv[2] == "follow":
            single_follow(sys.argv[3])
        else:
            pass
    else:
        pass
except:
    print("start.py <single|multi> <follow|like> [username]")