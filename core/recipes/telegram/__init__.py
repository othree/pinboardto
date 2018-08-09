import time
import requests


def to_telegram_bot(bookmarks, config):
    for chat_id in config['chat_ids']:
        r = requests.post('https://api.telegram.org/bot%s/getUpdates' % (config['api_token']))
        print(r.json())
        for bookmark in bookmarks:
            data = {
                "chat_id": chat_id,
                "text": '%s %s' % (bookmark['extended'] or bookmark['description'], bookmark['href'])
            }
            r = requests.post('https://api.telegram.org/bot%s/sendMessage' % (config['api_token']), data=data)
            print('%s post to telegram %s' % (bookmark['href'], config['name']))
            time.sleep(.500)