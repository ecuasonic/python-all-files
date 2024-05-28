import logging



logger = logging.getLogger(__name__) #we can use any name, but it is good practice to use '__name__' variable
#the __name__ variable will be assigned to the file name within the file itself, when imported to another file as a module
#if logger doesn't exist, then it will be created, similar to sqlite3.connect(file)
#filename = __name__ + '.log'

#The equivalent of setting logging.basicConfig to the root logger
logger.setLevel(logging.INFO) #sets level to logger ; the lowest level to be logged

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s') #create formatter object for logging 
file_handler = logging.FileHandler('employee.log') #creates file_handler object to specify the employee log file that we want to log to

file_handler.setFormatter(formatter) #to add format to fileHandler for logger

logger.addHandler(file_handler) #to add handler to logger 



#loggers are within a hierarchy
#    If the 'logger' logger has nothing configured, then it will fall back to the root logger's configurations (logname, levelname, format)
'''logging.basicConfig(filename='employee.log', level=logging.INFO, 
                   format='%(levelname)s:%(name)s:%(message)s') #This is configured to the 'logger' logger'''

#*****************now we use logger.info(str) instead of logging.info(str)*************************

class Employee:
    '''A sample Employee class'''

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey','Schafer')
emp_2 = Employee('Jane','Doe')