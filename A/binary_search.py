from util import time_it


# @time_it
def recursive_binary_search(array, value, start, finish):
    if start > finish:
        return -1

    mid_idx = (start + finish) // 2
    mid_value = array[mid_idx]

    if value == mid_value:
        return mid_idx

    elif value > mid_value:
        return recursive_binary_search(array, value, start + 1, finish)

    else:
        return recursive_binary_search(array, value, start, finish - 1)


# @time_it
def binary_search(array, value):
    pass
