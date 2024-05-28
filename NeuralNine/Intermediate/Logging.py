import logging

# Default security level is set at Warning 
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


logger.info("You have got 20 mails in your mailbox")
logger.critical("All components have failed")
logger.log(logging.ERROR, "An error occured!")