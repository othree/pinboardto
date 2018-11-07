import time
import requests


def getUpdates(api_token):
    r = requests.get('https://api.telegram.org/bot%s/getUpdates' % (api_token))
    try:
        msgs = r.json()['result']
    except Exception:
        msgs = []
        pass

    return msgs


def getChatId(msg):
    try:
        message = msg.get('message', msg.get('edited_message', None))
        return message['chat']['id']
    except Exception:
        return None


def getText(msg):
    return msg.get('message', {}).get('text', '')


def getChatTexts(chat_id, msgs):
    return [getText(msg) for msg in msgs if getChatId(msg) == chat_id]


def isPostedBefore(bookmark, texts):
    return bool(len([text for text in texts if text.find(bookmark['href']) >= 0]))


def to_telegram_bot(bookmarks, config):
    msgs = getUpdates(config['api_token'])
    for chat_id in config['chat_ids']:
        for bookmark in bookmarks:
            if isPostedBefore(bookmark, getChatTexts(chat_id, msgs)):
                continue

            data = {
                "chat_id": chat_id,
                "text": '%s %s' % (bookmark['extended'] or bookmark['description'], bookmark['href'])
            }
            r = requests.post('https://api.telegram.org/bot%s/sendMessage' % (config['api_token']), data=data)
            print('%s post to telegram %s [%s]' % (bookmark['href'], config['name'], r.status_code))
            time.sleep(.500)
