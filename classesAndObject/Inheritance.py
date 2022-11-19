from My_First_Class import MyClass


class MyNewClass(MyClass):

    def __init__(self, routername, model, serialno, ios, portno):
        MyClass.__init__(self, routername, model, serialno, ios)
        self.portno = portno

    def print_new_router(self, string):
        print(string + self.model)


newRouter = MyNewClass("Cisco", "2500", "23456", "13.0", "8080")

# Calling the superclasses members
newRouter.print_router("11.22.2020")
print(newRouter.model)

MyClass.set_name("Jerry")
MyClass.static_method()

