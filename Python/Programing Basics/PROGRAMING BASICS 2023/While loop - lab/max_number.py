from sys import maxsize

number = input()

MAX_NUMBER = -maxsize

while number != "Stop":
    num = int(number)
    if num > MAX_NUMBER:
        MAX_NUMBER = num
    number = input()
print(MAX_NUMBER)