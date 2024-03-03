text = input()

try:
    count = int(input())
    print(text * count)

except ValueError:
    print("Variable times must be an integer")