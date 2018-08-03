import requests
import pendulum


def normalize(bookmark):
    dt = pendulum.parse(bookmark['time'])
    bookmark['timestamp'] = int(dt.timestamp())
    return bookmark


def pinboard(config):
    r = requests.get('https://api.pinboard.in/v1/posts/recent&format=json&auth_token=%s' % (config['api_token']))
    bookmarks = r.json()['posts']
    return map(normalize, bookmarks)
