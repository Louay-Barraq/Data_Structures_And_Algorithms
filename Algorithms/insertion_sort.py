def insertion_sort(array):
    for i in range(1, len(array)):
        anchor = array[i]
        j = i - 1
        while j >= 0 and anchor < array[j]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
        array[j+1] = anchor

    return array
