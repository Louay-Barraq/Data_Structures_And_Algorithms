def selection_sort(array):
    for i in range(len(array) - 1):
        # find minimum value in the array
        min_index = array.index(min(array[i:]))
        # swap it with the first element in the current subarray
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

    return array
