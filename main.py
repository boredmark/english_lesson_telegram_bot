import time
from config import token
from bot import Bot


def bot_polling():
    my_bot = Bot(token)
    last_update_id = 0
    while True:
        try:
            time.sleep(1)
            last_update = my_bot.get_info_from_last_updates()
            if last_update['update_id'] > last_update_id:
                my_bot.send_massage(last_update['chat_id'],
                                    my_bot.process_massage(last_update['text'], last_update['user_id']))
            last_update_id = last_update['update_id']
        except Exception:
            continue


if __name__ == '__main__':
    bot_polling()







