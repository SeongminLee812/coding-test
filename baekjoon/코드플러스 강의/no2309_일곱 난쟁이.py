# 모든 수(7가지)를 더해서 100이 되면 됨
## 전체에서 (앞에서부터) 돌면서 2개 수를 빼서 100이 되면,
## 그 2개 수는 없어져야되는 수임
## 리스트에서 2개 뺴고 출력

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

all_len = sum(dwarfs)

def search():
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if all_len  - (dwarfs[i] + dwarfs[j]) == 100:
                a, b = dwarfs[i], dwarfs[j]
                dwarfs.remove(a)
                dwarfs.remove(b)
                return

search()
dwarfs.sort()
for d in dwarfs:
    print(d)