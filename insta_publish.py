import instabot
import os
import time
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def publish_on_instagram(photos):
    bot = instabot.Bot()
    bot.login(username=login, password=password)
    for photo in photos:
        try:
            bot.upload_photo(photo)
        except PermissionError:
            time.sleep(2)
            continue
