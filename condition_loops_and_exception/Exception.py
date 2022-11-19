list1 = [1, 2, 3, 4, 5, 6, 7]

for i in list1:
    try:
        print(list1[7])
    except IndexError as e:
        print(e, "Index out of bound")


try:
    print(4/0)
except ZeroDivisionError:
    print("Not allowed")
finally:
    print("I don't care, i'm getting printed anyway")
