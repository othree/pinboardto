import os
import time
import toml
import pendulum

from core.pinboard import pinboard
from core.recipts.telegram import to_telegram


OFFSET = 120
PERIOD = 60


dir = os.path.dirname(os.path.realpath(__file__))
conf_file = os.path.join(dir, 'conf.toml')

conf = toml.load(conf_file)


def validator(bookmark, start, end):
    return (bookmark['timestamp'] >= start and end > bookmark['timestamp'])


end = pendulum.now().second_(0).subtract(seconds=OFFSET)
start = int(end.subtract(seconds=PERIOD).timestamp())
end = int(end.timestamp())

bookmark_feeds = [pinboard(c) for c in conf['pinboard']]
bookmarks = [item for sublist in bookmark_feeds for item in sublist]
bookmarks = [item for item in bookmarks if validator(item, start, end)]

[to_telegram(bookmarks, c) for c in conf['to_telegram_bot']]
