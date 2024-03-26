"""
This decorator returns the multiplication of result of the func and the given decorator's argument.
"""
def multiply(times):

    def decorator(function):

        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times
        return wrapper

    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
