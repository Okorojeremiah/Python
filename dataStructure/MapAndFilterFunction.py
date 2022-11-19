# map takes a function and applies it on a sequence

def product(a):
    return a * 10

r1 = range(10)

print(map(product, r1))
print(list(map(product, r1)))

print(list(map(lambda a: a * 10, r1)))

# Filter takes a function and return the element for which the function is true 

print(list(filter(lambda a: a > 5, r1)))