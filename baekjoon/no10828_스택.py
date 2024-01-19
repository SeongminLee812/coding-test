# 스택 구현
## 딕셔너리에 명령어 넣기..?
# 명령어가 push 인 경우 x도 argument로 받아야함
import sys
input = sys.stdin.readline

n = int(input())
def is_empty(array):
    if array:
        print(0)
    else:
        print(1)

def size(array):
    print(len(array))

def pop(array):
    if array:
        print(array.pop())
    else:
        print(-1)

def top(array):
    if array:
        print(array[-1])
    else:
        print(-1)


array = []

for _ in range(n):
    a = input().rstrip()
    if a == 'top':
        top(array)
    elif a == 'size':
        size(array)
    elif a == 'pop':
        pop(array)
    elif a == 'empty':
        is_empty(array)
    else:
        a, x = a.split()
        array.append(int(x))


