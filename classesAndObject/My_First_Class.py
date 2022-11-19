class MyClass:

    name = None

    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number is: ", self.serialno)
        print("The ios version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)

    @classmethod
    def set_name(cls, name):
        cls.name = name

    @staticmethod
    def static_method():
        print(MyClass.name)


