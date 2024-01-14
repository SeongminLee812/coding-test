
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

print(binary_search([1, 2, 3, 4, 5, 6, 7], 2, 0, 6))
