from My_First_Class import MyClass

router = MyClass("R1", "2600", "123456", "12.4")

router.print_router("11.13.2022")

# Assigning a new value to the instance variable
router.serialno = "567893"
print(router.serialno)

# get and set function of python
print(getattr(router, "ios"))
setattr(router, "ios", "12.3")
print(getattr(router, "ios"))

# deleting an object attribute

delattr(router, "ios")
print(hasattr(router, "ios"))

# checking if an object is an instance of a class

print(isinstance(router, MyClass))
