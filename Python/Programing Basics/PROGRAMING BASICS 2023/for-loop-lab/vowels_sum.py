text = input()
value = 0

for n in text:
    if n == "a":
        value += 1
    elif n == "e":
        value += 2
    elif n == "i":
        value += 3
    elif n == "o":
        value += 4
    elif n == "u":
        value += 5
print(value)