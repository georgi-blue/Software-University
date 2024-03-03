numbers = [float(num) for num in input().split()]

num_dict = {}

for n in numbers:
    if n in num_dict.keys():
        num_dict[n] += 1
    else:
        num_dict[n] = 1

for number,counter in num_dict.items():
    print(f"{number} - {counter} times")