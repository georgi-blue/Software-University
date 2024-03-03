from collections import deque

water_quantity = int(input())
people_queue = deque()

name = input()

while name != "Start":
    people_queue.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        water_request = int(data[0])
        person = people_queue.popleft()
        if water_quantity >= water_request:
            print(f"{person} got water")
            water_quantity -= water_request
        else:
            print(f"{person} must wait")

    elif len(data) == 2:
        _, refill = data
        water_quantity += int(refill)
    command = input()

print(f"{water_quantity} liters left")