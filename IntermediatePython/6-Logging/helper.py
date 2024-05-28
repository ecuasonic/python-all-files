import logging

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(filename)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('file.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.propagate = False #makes it so that the root logger doesn't log this, and so that only the stream_logger logs it into console stream
logger.info('hello from helper')