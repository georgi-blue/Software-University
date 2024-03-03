command = input()
num1,num2 = int(input()), int(input())

def calc(command,num1,num2):
    if command == "multiply":
        return num1 * num2
    elif command == "divide":
        if num1 == 0 or num2 == 0:
            return "Error you can't divide by zero."
        else:
            return int(num1 / num2)
    elif command == "add":
        return num1 + num2
    elif command == "subtract":
        return num1 - num2

print(calc(command,num1,num2))