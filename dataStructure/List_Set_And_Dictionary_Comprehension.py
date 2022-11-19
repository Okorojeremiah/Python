# List comprehension
list1 = []

for i in range(10):
    result = i ** 2
    list1.append(result)

list2 = [x ** 2 for x in range(10)]

print(list2)
print(list1)

# Set comprehension

set1 = {x ** 2 for x in range(10)}
print(set1)

# Dictionary comprehension

dict1 = {x : x**2 for x in range(10)}
print(dict1)