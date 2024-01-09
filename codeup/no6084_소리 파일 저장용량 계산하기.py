h, b, c, s = map(int, input().split())

total = h * b * c * s
storage = total / ( 8 * 1024 * 1024)
print(f'{storage:.1f} MB')