import bisect

data = [108, 12, 9, 57, 30]
data.sort()

bisect.insort(data, 43)
print(data)

print(all([True, True, 1]))
