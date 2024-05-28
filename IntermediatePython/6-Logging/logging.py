import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s : %(filename)s', datefmt='%m/%d/%Y %H:%M:%S') 
#root logger configuration; cannot be overwritten

'''logging.debug('This is a debug message') 
logging.info('This is an info message') 
logging.warning('This is a warning message') 
logging.error('This is an error message') 
logging.critical('This is a critical message')'''
#These are the five logging types for messages

#if want to log in different modules, then it's best practice to not use this root logger, but to create your own logger in your module
#    This is because the root logger can only be configured once and cannot be overwritten to accomodate for other configurations (filename, levelname, format)

'''
import logging
logger = logging.getLogger(__name__)
#logger.propagate = False; not propogate to the base logger. Nothing gets logged in the base logger
logger.info('hello from helper')
'''
#import helper #runs helper, with the root configuration set here unless logger.propagation=False