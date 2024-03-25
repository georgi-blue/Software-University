"""
This decorator is created to execute the func only if the arguments are even numbers.
"""
def even_parameters(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, int) and arg % 2 == 0:
                continue

            return "Please use only even numbers!"

        return func(*args, **kwargs)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
