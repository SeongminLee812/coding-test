n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)

iteration = m // (k + 1)

iter01 = iteration * ((array[0] * k) + (array[1] * 1))
iter02 = m % (k + 1)
print(iter01 + (iter02 * array[0]))



