list1 = []
print(type(list1))

list1 = ["Jerry", 1991, 2, 12, "Okoro", "Otitodilichukwu"]

print(len(list1))

print(list1[0])

# Slicing list

print(list1[: 3])
print(list1[-4: -1])
print(list1[::-1])

# Adding an element

list1.append("Jayblinks")
print(list1)

#Adding an element at a particular index

list1.insert(2, "Eze")
print(list1)

# Removing an element

print(list1.pop(3))

# Adding two list
list2 = [2, 3, 5, 7]
list1.extend(list2)
print(list1)

# list sorting

list2.sort()
print(list2)

list2.reverse()
print(list2)

print(list2.count(5))

print(sorted(list2))
print(sorted(list2, reverse=True))



