my_turple = (9, 3, 5, 6, 7)

print(type(my_turple))

# Turple unpacking
turple1 = ("cisco", "2600", "12.4")
(vendor, model, ios) = turple1

print(vendor)
print(model)
print(ios)

# Assigning values in a turple to another values in a turple
(a, b, c) = (1, 2, 3)
print(a)
print(b)
print(c)

del turple1
print(turple1)