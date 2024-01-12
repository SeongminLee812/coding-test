n = int(input())

coin_types = [500, 100, 50, 10, 5, 1]

count = 0
n = 1000 - n

for coin in coin_types:
    if n >= coin:
        count += n // coin
        n %= coin

print(count)