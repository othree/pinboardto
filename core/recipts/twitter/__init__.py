import time
import twitter


def to_twitter(bookmarks, config):
    api = twitter.Api(consumer_key=config['consumer_key'],
                      consumer_secret=config['consumer_secret'],
                      access_token_key=config['access_token_key'],
                      access_token_secret=config['access_token_secret'])

    for bookmark in bookmarks:
        r = api.PostUpdate('%s %s' % (bookmark['extended'] or bookmark['description'], bookmark['href']))
        print('%s post to twitter %s' % (bookmark['href'], config['name']))
        time.sleep(.500)
