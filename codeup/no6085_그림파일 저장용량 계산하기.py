w, h, b = map(int, input().split())

total = w * h * b
storage = total / (8 * 1024 * 1024)

print(f'{storage:.2f} MB')