import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        finish_time = time.time()

        print(func.__name__ + " took " + str((finish_time - start_time)*1000) + " mil seconds")
    return wrapper
