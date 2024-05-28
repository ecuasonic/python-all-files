#Process pool can be used to manage multiple processes
#    Controls a pool of worker processes to which jobs can be submitted
#    It can split data into smaller chucks, which can then be processed in parallel by different processes

from multiprocessing import Pool

def cube(number):
    return number * number * number


if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    map_result = pool.map(cube, numbers)
    #*********USED TO APPLY FUNCTION TO EACH ELEMENT IN LIST*******************
    #Automatically allocate the maximum number of available processes and create different processes 
    #   Parallel Execution
    #   it will then split the iterable into equal sized-chucks
    #   then it will submit each one into the function
    #   The function will then be executed in parallel by different processes

    apply_result = [pool.apply(cube, (num,)) for num in numbers]
    # Execute a seperate process with this function with one argument 
    # Serial Execution

    pool.close() # should call pool.close() before pool.join()

    pool.join() # wait for pool to process all the calculations and result

    print(map_result, apply_result)