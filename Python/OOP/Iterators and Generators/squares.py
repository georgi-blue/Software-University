def squares(n: int):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1

print(list(squares(5)))