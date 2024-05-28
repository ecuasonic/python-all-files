import logging
import logging.config

logging.config.fileConfig('log.conf')
#This applies the configurations to the loggers root and simpleExample
#We can use another file to set up and modify the configurations

#There is also logging.config.dictConfig()

logger = logging.getLogger('simpleExample')
logger.debug('This is a debug message')