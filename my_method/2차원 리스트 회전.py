def rotate_a_matrix_by_90_degree(matrix):
    n = len(matrix) # 행 길이 계산
    m = len(matrix[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 회전이니까 n과 m의 위치가 다름
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result