numbers = []

num_functions = {
    "1": lambda x: numbers.append(x[1]),
    "2": lambda x: numbers.pop() if numbers else None,
    "3": lambda x: print(max(numbers)) if numbers else None,
    "4": lambda x: print(min(numbers)) if numbers else None,
    }


for _ in range(int(input())):
    number_data = input().split()
    command = number_data[0]
    num_functions[command](number_data)

numbers.reverse()

print(*numbers, sep=", ")

