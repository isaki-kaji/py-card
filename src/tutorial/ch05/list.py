print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y if x > y])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

print([num for num in range(0, 10) if num != 3])
