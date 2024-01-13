# https://www.acmicpc.net/problem/1541
# 아이디어 '-'를 만난 이후에는 전부 다 빼기만 하면 됨.


data = input()

minus_index = data.find('-')

result = 0

temp = ''
if minus_index == -1:
    for i in range(len(data)):
        if not data[i].isdigit():
            result += int(temp)
            temp = ''
        else:
            temp += data[i]
        if i == len(data) - 1:
            result += int(temp)
else:
    for i in range(minus_index):
        if not data[i].isdigit():
            result += int(temp)
            temp = ''
        else:
            temp += data[i]
        if i == minus_index - 1:
            result += int(temp)

    temp = ''
    for j in range(minus_index + 1, len(data)):
        if not data[j].isdigit():
            result -= int(temp)
            temp = ''
        else:
            temp += data[j]
        if j == len(data) - 1:
            result -= int(temp)

print(result)



