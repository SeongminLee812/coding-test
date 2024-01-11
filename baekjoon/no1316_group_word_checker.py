n = int(input())
def check(string: str) -> bool:
    s_set = set()
    for i in range(1, len(string)):
        if string[i - 1] != string[i]:
            s_set.add(string[i - 1])
        if string[i] in s_set:
            return False
    return True

result = 0

for _ in range(n):
    string = input()
    if check(string):
        result += 1

print(result)