import time


def time_it(func, iterations, *args, **kargs):
    """
    Function to measure time elapsed by a function
    """
    start = time.time()
    for i in range(iterations):
        func(*args, **kargs)
    stop = time.time()
    return (stop - start) / iterations
