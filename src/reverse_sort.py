"""
sort given array in reverse order using insertion sort.
The time complexity will be O(n^2) for the upper bound.
"""


def reverse_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(reverse_insertion_sort([31, 41, 59, 26, 41, 58]))
