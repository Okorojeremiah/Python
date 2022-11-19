def my_decorator(target_function):
    def function_wrapper():
        return "Python is the " + target_function() + " language"

    return function_wrapper


@my_decorator
def target_function():
    return "best"


print(target_function())
