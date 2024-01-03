array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # quit if the number of element is 0
        return
    pivot = start # first element
    left = start + 1
    right = end
    while left <= right:
        # repeat until seek data bigger than pivot
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # repeat until seek data which is smaller than pivot
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # if cross, swap pivot and smaller data
            array[right], array[pivot] = array[pivot], array[right]
        else: # if not cross, swap smaller data and bigger data
            array[left], array[right] = array[right], array[left]
    # after divide, sorting each partition
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array):
    # quit if len(list) <= 1
    if len(array) <= 1:
        return array

    pivot = array[0] # first element of array
    tail = array[1:] # all element without pivot

    left_side = [x for x in tail if x <= pivot] # left side after devide
    right_side = [x for x in tail if x > pivot] # right side after devide

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

