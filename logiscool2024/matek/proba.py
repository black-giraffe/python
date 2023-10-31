komb = []
from itertools import combinations
numbers = list(range(1, 16))
unique_combinations = set(combinations(numbers, 4))
for combination in unique_combinations:
    komb.append(combination)


print(komb)
print(len(komb))
print(komb[0][2])
print(komb[0][0])