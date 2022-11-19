# Iterator
my_list = [1, 2, 3, 4, 5, 6, 7]

my_iter = iter(my_list)

print(next(my_iter))


# Generator

def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y


gen = my_gen(5, 6)
print(next(gen))
print(next(gen))

# Generator expression

gen_exp = (x for x in range(10))
print(type(gen_exp))

print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
