import logging

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info = True) #logging.exception(e) does the same thing

import traceback
try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())