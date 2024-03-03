def even_odd(*numbers):
    command = numbers[-1]

    if command == "even":
        return [n for n in numbers[:-1] if n % 2 == 0]
    else:
        return [n for n in numbers[:-1] if n % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))