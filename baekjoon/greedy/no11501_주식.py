t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    rev = prices[::-1]

    max_price = 0
    profit = 0

    for i in range(len(prices)):
        max_price = max(max_price, rev[i])
        profit += max_price - rev[i]

    print(profit)