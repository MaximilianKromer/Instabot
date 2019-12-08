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


def auto_accept():
    cfg = load_config.load_json()
    path = cfg['general'].get('driver_path')
    username = cfg['single_bot'].get('username')
    password = cfg['single_bot'].get('password')
    timeout = cfg['general'].get('auto_accept').get('timeout')

    print("--- Auto accept all follow requests ---")
    print("stop it by pressing CTRL+C")
    print("")
    print("Log:")

    bot = SingleAccountBot(username=username, password=password, path=path)
    time.sleep(2)
    while True:
        bot.open_followlist()
        time.sleep(2)
        bot.accept_follows()
        time.sleep(timeout)


def debug():
    cfg = load_config.load_json()
    path = cfg['general'].get('driver_path')
    username = cfg['single_bot'].get('username')
    password = cfg['single_bot'].get('password')

    bot = SingleAccountBot(username=username, password=password, path=path)
    time.sleep(3)
    bot.open_followlist()
    time.sleep(20)
    bot.close()


def show_help():
    print("Command not found")
    print("Usage:")
    print("  start.py <single|multi> <follow|like|auto_accept> [username]")
    print("")
    print("Warning: Account List (Multi) currently not supported")


try:
    if sys.argv[1] == "single":
        if sys.argv[2] == "follow":
            single_follow(sys.argv[3])
        elif sys.argv[2] == "auto_accept":
            auto_accept()
        else:
            show_help()
    elif sys.argv[1] == "multi":
        show_help()
    elif sys.argv[1] == "debug":
        debug()
    else:
        show_help()
except:
    show_help()