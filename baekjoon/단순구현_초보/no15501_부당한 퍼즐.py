n = int(input())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

def check_same(array_a, array_b):
    a_index = array_a.index(1)
    b_index = array_b.index(1)

    new_a = array_a[a_index:] + array_a[:a_index]
    new_b = array_b[b_index:] + array_b[:b_index]
    if new_a == new_b:
        return True

    # 뒤집어서 체크
    array_b = array_b[::-1]

    b_index = array_b.index(1)
    new_b = array_b[b_index:] + array_b[:b_index]
    if new_a == new_b:
        return True
    return False

if check_same(array_a, array_b):
    print('good puzzle')
else:
    print('bad puzzle')

