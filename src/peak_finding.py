"""
Peak finding:
------------------------
 ex: if the given array is [5, 3, 2, 9] the local peak value will be 2 
 Finding peak value: The number which is surrounded by greater than or equal to that number.
"""


def find_local_peak(arr):
    for i in range(1, len(arr)-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return arr[i]


print(find_local_peak([3,4,5,6,7,6,5,4]))
