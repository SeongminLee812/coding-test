string = input()
d = [0] * 26

for s in string:
    i = ord(s) - ord('a')
    d[i] += 1

print(*d)