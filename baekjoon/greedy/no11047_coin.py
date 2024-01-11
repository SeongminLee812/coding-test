import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins = coins[::-1]

count = 0

for coin in coins:
    if k >= coin:
        count += k // coin
        k %= coin

print(count)