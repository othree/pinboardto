import time
import twitter


def to_twitter(bookmarks, config):
    api = twitter.Api(consumer_key=config['consumer_key'],
                      consumer_secret=config['consumer_secret'],
                      access_token_key=config['access_token_key'],
                      access_token_secret=config['access_token_secret'])

    for bookmark in bookmarks:
        text = bookmark['extended'] or bookmark['description'] or ''
        text = text[:128]
        r = api.PostUpdate('%s %s' % (text, bookmark['href']))
        print('%s post to twitter %s' % (bookmark['href'], config['name']))
        print(status)
        time.sleep(.500)
