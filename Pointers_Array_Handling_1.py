import numpy as np
def search_array(array, target):
    left, right = 0, len(array) -1
    array = np.sort(array)
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_array_2(array, target):
    pointer = 0

    while pointer <= len(array):
        if  array[pointer] == target:
            return pointer
        else:
            pointer += 1
    return -1


print("search_array:", search_array([23,56,1,34,67,99,3], 56))
#print("search_array_2:",search_array_2([23,56,1,34,67,99,3], 10))
