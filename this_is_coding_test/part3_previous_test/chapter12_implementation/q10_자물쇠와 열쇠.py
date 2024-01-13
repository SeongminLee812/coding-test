
lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]


from typing import *
# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(matrix: List[List]) -> List[List]:
    n = len(matrix) # 행 길이 계산
    m = len(matrix[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 회전이니까 n과 m의 위치가 다름
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result

# 자물쇠와 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙에 자물쇠 끼워 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 열쇠가 맞는 지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

 
print(solution(key, lock))