first_lambda = lambda x, y: x * y

print(first_lambda(5, 4))


def concat_list(mylist):
    list1 = []
    for i in range(10):
        for x in range(10):
            result = i * x
            list1.append(result)
    return list1 + mylist


second_lambda = lambda mylist: [i * j for i in range(10) for j in range(10)] + mylist

print(concat_list([100, 101, 102]))
print(second_lambda([100, 101, 102]))
