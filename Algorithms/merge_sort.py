def merge_arrays(array_1, array_2):
    sorted_array = []
    len_1, len_2 = len(array_1), len(array_2)
    i, j = 0, 0

    while i < len_1 and j < len_2:
        if array_1[i] < array_2[j]:
            sorted_array.append(array_1[i])
            i += 1
        elif array_1[i] > array_2[j]:
            sorted_array.append(array_2[j])
            j += 1
        else:
            sorted_array.append(array_1[i])
            sorted_array.append(array_2[j])
            i += 1
            j += 1

    while i < len_1:
        sorted_array.append(array_1[i])
        i += 1

    while j < len_2:
        sorted_array.append(array_2[j])
        j += 1

    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_arrays(left, right)
