list = [3, 3, 4, 5, 4, 6, 7, 8, 5]
set1 = set(list)
print(set1)

set1.add(34)
print(set1)

set2 = {2, 3, 4, 5, 6, 3, 2}
print(set2)

set2.remove(2)
print(set2)

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))
print(set1.pop())
set1.clear()
print(set1)