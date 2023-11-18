def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    smaller, equal, bigger = [], [], []

    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            bigger.append(x)

    return quick_sort(smaller) + equal + quick_sort(bigger)
