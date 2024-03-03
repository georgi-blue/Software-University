import os

path = os.path.join("numbers.txt")
file = open(path)
total_sum = 0

lines = file.readlines()
file.close()

for line in lines:
    total_sum += int(line.strip())

print(total_sum)