def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
    return None

##### Tests
#print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(binary_search([10, 12, 23, 48, 53, 68, 70, 88, 92, 101], 68))
