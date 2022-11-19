from itertools import *

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 5, 6, 7, 8, 6, 7]

# Concatenate two list
for i in chain(list1, list2):
    print(i)

print(list(chain(list1, list2)))

# produce an infinite loop unless we add a break
for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break

# receives a function and returns the element for which the element is not true
filterfalse(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7])
print(list(filterfalse(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7])))

# islice returns a substring

a = islice(range(10), 2, 9, 2)
print(list(a))
