
n = int(input())
data = []
for _ in range(n):
    data.append(input())

if n == 1:
    print(data[0])
else:
    result = ""
    for i in range(len(data[0])):
        my = data[0][i]
        for s in data:
            if my != s[i]:
                my = '?'
                break
        result += my

    print(result)