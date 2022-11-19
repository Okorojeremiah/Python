# def my_first_function():
#     """This is our first function!"""
#     print("Hello python!")
#
#
# my_first_function()
#
#
# def my_second_function(x):
#     print(x)
#
#
# my_second_function("I love Java")
#
#
# def my_third_function(x, y):
#     return x * y
#
#
# print(my_third_function(2, 3))
#
#
# def add(list1, list2):
#     div = 0
#     total = []
#     count = len(list1) - 1
#
#     for i in list1:
#         my_sum = (list1[count] + div) + list2[count]
#         if my_sum > 9 and count != 0:
#             modulo = my_sum % 10
#             div = my_sum / 10
#             total.append(modulo)
#         else:
#             total.append(my_sum)
#         count -= 1
#     return total[::-1]
#
#
# my_list = [1, 2, 3, 4]
# my_list2 = [3, 4, 5, 6]
# print(add(my_list, my_list2))


# defining a function with multiple args

# def funct(x, *args):
#     print(x)
#     for i in args:
#         print(i)
#
#
# funct(1, 2, 3, 4, 5, 6, 7, 8)


def funct2(x, **kwargs):
    print(x)
    for keys in kwargs:
        print("The key {} holds {} value".format(keys * 2, kwargs[keys] * 2))


funct2(2, name="Jerry", age=5)


def funct3():
    my_var = 10
    return my_var


result = funct3()

print(result * 10)

if __name__ == "__main__":
    print("Done")
