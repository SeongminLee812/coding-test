def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 0, 11))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None



print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3, 0, 11))