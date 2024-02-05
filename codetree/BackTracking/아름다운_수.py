n = int(input())
ans = []
total = 0

def choose(index):
    global total
    if index == n:
        print(' '.join(map(str, ans)))
        total += 1
        return
    if index > n:
        return
    for i in range(1, 5):
        ans.append(i)
        choose(index + 1)
        ans.pop()