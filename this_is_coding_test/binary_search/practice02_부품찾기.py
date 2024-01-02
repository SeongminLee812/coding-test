# import sys
# n = int(input())
# my_part = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(input())
# seeking_part = list(map(int, sys.stdin.readline().rstrip().split()))
# my_part.sort()
#
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
# for i in range(m):
#     result = binary_search(my_part, seeking_part[i], 0, n)
#     if result:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
#
# # 교재 답안
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif target > array[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
# n = int(input())
# array = list(map(int, sys.stdin.readline().rstrip().split()))
# array.sort()
# m = int(input())
# seeking_array = list(map(int, sys.stdin.readline().rstrip().split()))
#
# for i in seeking_array:
#     result = binary_search(array, i, 0, n - 1)
#     if result:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


# 계수 정렬 이용

# n = int(input())
# array = [0] * 100001
#
# # 가게에 있는 전체 부품 번호를 입력받아서 기록
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
#
# # 손님이 확인 요청한 부품 번호를 하나씩 확인
# for i in x:
#     if array[i]:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')


# 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
