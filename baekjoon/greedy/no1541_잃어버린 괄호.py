# https://www.acmicpc.net/problem/1541

# 아이디어 '-'를 만난 이후에는 전부 다 빼기만 하면 됨.

data = input()

minus_index = data.find('-')

result = 0

temp = ''
if minus_index == -1:
    for d in data:
        if not d.isdigit():
            result += int(temp)
        else:
            temp += d



