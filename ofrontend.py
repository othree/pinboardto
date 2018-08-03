import os
import time
import toml
import pendulum
from pendulum import timezone

from lib.pinboard import pinboard

RECIPTS = ['twitter', 'telegram']

OFFSET = 120
PERIOD = 120


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


print(bookmarks)
