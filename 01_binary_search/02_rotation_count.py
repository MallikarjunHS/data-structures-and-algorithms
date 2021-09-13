# Given a circularly sorted integer array, find the total number of positions array is rotated. 
# Assume there are no duplicates in the array, and rotation is in anti clockwise direction
# source: https://www.techiedelight.com/find-number-rotations-circularly-sorted-array/

def count_rotations_linear(arr):
    i = 0
    while i != len(arr)-1:
        if arr[i] < arr[i+1]:
            i += 1
        else:
            return i+1
    if i != len(arr)-1:
        return i
    else:
        return 0

def count_rotations_binary(arr):
    l = 0
    h = len(arr)-1
    while l <= h:
        mid = l+(h-l)//2
        mid_element = arr[mid]
        if arr[l] > arr[h] < arr[h-1]:
            return h
        elif arr[l+1] > arr[l] < arr[h]:
            return l
        elif arr[mid-1] > mid_element < arr[mid+1]:
            return mid
        elif mid_element < arr[mid+1] and mid_element > arr[mid-1]:
            h = mid-1
        else:
            l = mid+1


def count_rotation_binary_simplified(arr):
    l = 0
    h = len(arr)-1
    while arr[l] > arr[h]:
        mid = l+(h-l)//2
        mid_element = arr[mid]
        high_element = arr[h]
        if  mid_element > high_element:
            l = mid+1
        else:
            h = mid
    return l

arr = [1, 2]
print(count_rotations_binary(arr))
