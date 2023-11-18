from util import time_it


# @time_it
def linear_search(array, value):
    for idx, element in enumerate(array):
        if element == value:
            return idx

    return -1
