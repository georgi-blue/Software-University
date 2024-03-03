number_list = input().split()

my_list = []

for number in number_list:
    my_list.append(abs(float(number)))

print(my_list)