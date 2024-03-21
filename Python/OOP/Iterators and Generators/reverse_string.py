def reverse_text(string: str):
    start_idx = len(string) - 1

    while start_idx >= 0:
        yield string[start_idx]
        start_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
