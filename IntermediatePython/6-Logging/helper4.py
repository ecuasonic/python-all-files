import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')

from logging.handlers import TimedRotatingFileHandler
import time

#s, m, h, d, midnight, w0 is Monday, w1 is Tuesday, ect.
handler2 = TimedRotatingFileHandler('timed_test.log', when='s', interval=5,backupCount=5)
logger.addHandler(handler2)

for _ in range(6):
    logger.info('Hello, World!')
    time.sleep(5)