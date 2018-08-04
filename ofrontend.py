import os
import time
import toml
import pendulum

from core.pinboard import pinboard
from core.recipts.telegram import to_telegram_bot
from core.recipts.twitter import to_twitter


dir = os.path.dirname(os.path.realpath(__file__))
conf_file = os.path.join(dir, 'conf.toml')

conf = toml.load(conf_file)
main_conf = conf.get('main', {})

OFFSET = main_conf.get('offset', 120)
PERIOD = main_conf.get('period', 60)

end_time = pendulum.now().set(second=0).subtract(seconds=OFFSET)
start = int(end_time.subtract(seconds=PERIOD).timestamp())
end = int(end_time.timestamp())


def validator(bookmark, start, end):
    return (bookmark['timestamp'] >= start and end > bookmark['timestamp'])


bookmark_feeds = [pinboard(c) for c in conf['pinboard']]
bookmarks = [item for sublist in bookmark_feeds for item in sublist]
bookmarks = [item for item in bookmarks if validator(item, start, end)]

[to_telegram_bot(bookmarks, c) for c in conf['to_telegram_bot']]
[to_twitter(bookmarks, c) for c in conf['to_twitter']]
