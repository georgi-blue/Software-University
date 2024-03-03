from sys import maxsize

number = input()

MIN_NUMBER = maxsize

while number != "Stop":
    num = int(number)
    if MIN_NUMBER > num:
        MIN_NUMBER = num
    number = input()
print(MIN_NUMBER)