def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a, b = map(int, input().split())

gcd_val = gcd(a, b)
print(gcd_val)
print(a * b // gcd_val)