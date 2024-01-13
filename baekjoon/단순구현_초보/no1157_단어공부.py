from collections import defaultdict
import sys
input = sys.stdin.readline

count_dict = defaultdict(int)

strings = input().rstrip().lower()

for s in strings:
    count_dict[s] += 1


values = list(count_dict.values())
max_count = max(values)

if values.count(max_count) > 1:
    print('?')
else:
    sorted_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dict[0][0].upper())