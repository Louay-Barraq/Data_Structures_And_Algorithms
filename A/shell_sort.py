def shell_sort(array):
    length = len(array)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            anchor = array[i]
            j = i
            while j >= gap and array[j - gap] > anchor:
                array[j] = array[j - gap]
                j -= gap
            array[j] = anchor
        gap //= 2

    return array
