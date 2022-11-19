set1 = {3, 4, 5, 6}
frozenSet1 = frozenset(set1)

set2 = {5, 4, 7, 2}
frozenSet2 = frozenset(set2)

print(frozenSet1.intersection(frozenSet2))
print(frozenSet1.union(frozenSet2))
print(frozenSet1.difference(frozenSet2))
