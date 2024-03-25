"""
This decorator is used to check the argument of the func is instance of the given decorator argument.
"""
def type_check(wanted_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(*args, wanted_type):
                return "Bad Type"

            return func(*args, **kwargs)

        return wrapper

    return decorator




@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
