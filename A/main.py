import random

from linear_search import linear_search
from binary_search import recursive_binary_search, binary_search
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort import shell_sort
from selection_sort import selection_sort


VALUES = [num for num in range(20)]


def random_values_generator():
    return [random.randint(1, 50) for _ in range(20)]


def linear_search_test(value):
    if linear_search(VALUES, value) != -1:
        print(f"Value: {value} exists in the array.")
    else:
        print(f"Value: {value} doesn't exist in the array.")


def recursive_binary_search_test(value):
    if recursive_binary_search(VALUES, value, 0, len(VALUES) - 1) != -1:
        print(f"Value: {value} exists in the array.")
    else:
        print(f"Value: {value} does not exist in the array")


def binary_search_test(value):
    if binary_search(VALUES, value) != -1:
        print(f"Value: {value} exists in the array.")
    else:
        print(f"Value: {value} does not exist in the array")


def bubble_sort_test():
    random_values = list(set(random_values_generator()))
    print(f"Array before sorting: {random_values}")
    print(f"Array after sorting: {bubble_sort(random_values)}")


def quick_sort_test():
    random_values = list(set(random_values_generator()))
    print(f"Array before sorting: {random_values}")
    print(f"Array after sorting: {quick_sort(random_values)}")


def insertion_sort_test():
    random_values = list(set(random_values_generator()))
    print(f"Array before sorting: {random_values}")
    print(f"Array after sorting: {insertion_sort(random_values)}")


def merge_sort_test():
    random_values = list(set(random_values_generator()))
    print(f"Array before sorting: {random_values}")
    print(f"Array after sorting: {merge_sort(random_values)}")


def shell_sort_test():
    random_values = list(set(random_values_generator()))
    print(f"Array before sorting: {random_values}")
    print(f"Array after sorting: {shell_sort(random_values)}")


def selection_sort_test():
    random_values = list(set(random_values_generator()))
    print(f"Array before sorting: {random_values}")
    print(f"Array after sorting: {selection_sort(random_values)}")


if __name__ == "__main__":
    tester = 7
    # linear_search_test(tester)
    # binary_search_test(tester)
    # recursive_binary_search_test(tester)
    # bubble_sort_test()
    # quick_sort_test()
    # insertion_sort_test()
    # merge_sort_test()
    # shell_sort_test()
    selection_sort_test()
