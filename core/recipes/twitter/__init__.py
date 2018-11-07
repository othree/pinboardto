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
        url = bookmark['href']

        if url.find('https://twitter.com') == 0:
            attachment_url = url
        else:
            text = '%s %s' % (text, url)
            attachment_url = None

        r = api.PostUpdate(text, attachment_url=attachment_url)
        print('%s post to twitter %s' % (bookmark['href'], config['name']))
        print(status)
        time.sleep(.500)
