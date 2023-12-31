from pprint import pprint

def solution(n):
    answer = [[]]
    answer = [[0 for _ in range(n)] for _ in range(n)]

    num = 0
    row = 0
    col = 0
    while True:
        num += 1
        if answer[row][col] == 0:
            answer[row][col] = num
            col += 1


    return answer


pprint(solution(5))