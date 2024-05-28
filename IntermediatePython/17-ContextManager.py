# Context managers are a great tool for resource management
#     They allow for allocation and release resources precisely when you want to

with open('notes.txt' ,'w') as file:
    file.write('some todoo...')
    # When we leave this "with" statement again, the context manager will make sure to correctly close the file
    #     Even if there was an exception inside the "with" paragraph

# "With" Statement Equivalent
file = open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close()



from threading import Lock
lock = Lock()

with lock:
    '''...'''


# "With" Statement Equivalent
lock.acquire()
#...
lock.release()



class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file: # if not none:
            self.file.close()
        if exc_value is not None:
            print('exception has been handled')
        #print('exc:', exc_type, exc_value)
        print('exit')
        return True # allows the "With" statement to continue past exceptions

with ManagedFile('notes.txt') as file:
    # as soon as object enters the "with" statement, __enter__() function is called
    print('do some stuff...')
    file.somemethod()
    # The "With" statement assigns the exception type to exc_type, exception value to exc_value, and the exception traceback to exc_traceback
    #    Otherwise the value is none and no exception is raised
    file.write('some todoo...')
    # just before leaving "with" statement, __exit()__ is called and closes the file, even exception is raised

print('Continuing')

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f 
        # When the "with" clause first calls on generator, f is returned, then stops here for further input
        # The "with" clause continues
        # Once the "with" clause exits, the generator is called again, which continues and closes the file
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todoo')
