def swap(a, b, arr):
    tmp = arr[a]
    a = arr[b]
    b = tmp


def bubble_sort(array):
    length = len(array)

    for i in range(length):
        all_swapped = True
        for j in range(length - (i + 1)):
            if array[j] > array[j+1]:
                # Swap items
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
                all_swapped = False

        if all_swapped:
            break

    return array
