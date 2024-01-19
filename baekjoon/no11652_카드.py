from collections import Counter

n = int(input())

cards = []

for _ in range(n):
    cards.append(int(input()))

counts = Counter(cards)
results = counts.most_common()
results.sort(key = lambda x: (-x[1], x[0]))
print(results[0][0])
