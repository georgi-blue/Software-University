n = int(input())
word = input()
strings = []
new_strings = []

for num in range(n):
    current_string = input()
    strings.append(current_string)

    if word in current_string:
        new_strings.append(current_string)

print(strings)
print(new_strings)



