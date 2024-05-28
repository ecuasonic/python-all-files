import logging
import employee #importing a module will run it
#The employee module is run. If configured, the root logger will be configured to filename = 'employee.log', level=logging.INFO, and format = ~~
#Once configured, the root logger will not be configured again. 
#Then only logs with INFO level and beyond will be logged into 'employee.log', excluding DEBUG level logs

#This is why we need a new logger for both modules, in order to configure seperately

 # DEBUG: Detailed information, typically of interest only when diagnosing problems
 # INFO: Confirmation that things are working as expected
 # WARNING: An indication that somthing unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
 # ERROR: Due to a more serious problem, the software has not been able to perform some function.
 # CRITICAL: A serious error, indicating that the program itself may be unable to continue running.




logger = logging.getLogger(__name__) #we can use any name, but it is good practice to use '__name__' variable
#the __name__ variable will be assigned to the file name within the file itself, when imported to another file as a module
#if logger doesn't exist, then it will be created, similar to sqlite3.connect(file)
#A logger represents a named object that can be used to log messages

#The equivalent of setting logging.basicConfig to the root logger
logger.setLevel(logging.DEBUG) #this method is used to set the logging level for a logger object
#sets the threshold level for the logger ; lower level messages will be ignored

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s') #create formatter object for logging file_handler 

file_handler = logging.FileHandler('sample.log') #creates file_handler object to specify the employee log file that we want to log to
#A FileHandler is responsible for writing log messages to a file
file_handler.setLevel(logging.ERROR) #this method is used to set the logging level for a FileHandler object
#sets the threshold level for the FileHandler ; lower level messages will be ignored
file_handler.setFormatter(formatter) #to add format to fileHandler for logger

#The file handler will only log the important messages to the file
#    while the logger itself can process more detailed lower-level messages.
#You might have multiple handlers attached to the logger, and each handler has its own specfic logging level
#    In such cases, the logging level would be set for each handler individually using the 'setLevel()' method. 

stream_handler = logging.StreamHandler() #logs to the console stream
#This is already set to DEBUG
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler) #to add file_handler to logger
logger.addHandler(stream_handler) #to add stream_handler to logger




'''logging.basicConfig(filename='sample.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(name)s:%(message)s') '''
#level=logging.DEBUG will cause debugs to be printed out/logged
#in combination with filename='test.log', nothing will be printed out, but will instead be logged into 'test.log'; each run will be logged into 'test.log'
#format='%(asctime)s:%(levelname)s:%(message)s' will print/log out '2023-07-13 21:01:41,801:DEBUG:Add: 10 + 5 = 15'
#    the name (of the logger) in %(name)s ; ex. root
#        If a specific logger is not specified, then it would log into the root logger ; best to log to specific loggers that can all be configured sperately
#    the level (of the loggee) in %(levelname)s ; ex. INFO 

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero') #using logging.expection rather than logging.error gives more information about traceback error
        #everything that wouldv'e been logged by logging.error is logged by logging.exception
    else: #This else runs if no exceptions are caught
        return result

num_1 = 10
num_2 = 0

#Logging level = debug, info, warning, ...

add_result = add(num_1, num_2)
logger.debug(f'Add: {num_1} + {num_2} = {add_result}') #if the logger is set to DEBUG and the handler 'logger' is set to ERROR, then this line won't be logged but will still be processed

sub_result = subtract(num_1, num_2)
logger.debug(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logger.debug(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logger.debug(f'Div: {num_1} / {num_2} = {div_result}')