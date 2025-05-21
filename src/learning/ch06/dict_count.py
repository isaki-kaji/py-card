from collections import defaultdict

data = ['apple', 'orange', 'melon']
result = defaultdict(int)

for key in data:
    result[key] += 1
