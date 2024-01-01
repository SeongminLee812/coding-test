def change(won: int) -> int:
    coin500, remain = divmod(won, 500)
    coin100, remain = divmod(remain, 100)
    coin50, remain = divmod(remain, 50)
    coin10, remain = divmod(remain, 10)

    return sum([coin500, coin100, coin50, coin10])

print(change(1260))

def change(n: int) -> int:
    coin_types = [500, 100, 50, 10]
    count = 0
    for coin in coin_types:
        count += n // coin
        n %= coin
    return count

print(change(1260))
