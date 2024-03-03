def multiply(*args):
    total_multiplier = 1

    for el in args:
        total_multiplier *= el

    return total_multiplier

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
