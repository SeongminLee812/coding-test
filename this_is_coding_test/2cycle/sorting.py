from typing import *
import sys
def selection_sort(array: List[any]) -> List[any]:
    for i in range(0, len(array)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array

print(selection_sort([1, 5, 7, 3, 2, 5, 3, 5]))

def insertion_sort(array: List[any]) -> List[any]:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array

print(insertion_sort([5, 7, 3, 2, 5, 3, 5, 1, 12, 4]))

def quick_sort(array: List[any]) -> List[any]:
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort([5, 7, 3, 2, 5, 3, 5, 1, 12, 4]))

def count_sort(array: List[any]) -> List[any]:
    count = [0] * (max(array) + 1)
    for i in array:
        count[i] += 1

    result = []
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)
    return result

print(count_sort([5, 7, 3, 2, 5, 3, 5, 1, 12, 4]))

