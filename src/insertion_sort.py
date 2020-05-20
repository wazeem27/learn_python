"""Insertion sort


Worst complexity: O(n^2)
Average case: O(n^2)      
Best case: O(n)

Space complexity: O(1)
"""



def insertion_sort(arr):
    """Insertion sort"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


print(insertion_sort([23, 45, 17, 12, 58, 12, 11, 98, 6, 10]))
