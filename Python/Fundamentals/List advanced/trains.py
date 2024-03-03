wagons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break

    elif command[0] == "add":
        new_people = int(command[1])
        wagons[-1] += new_people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people

    elif command [0] == "leave":
        leaved_index = int(command[1])
        leaved_people = int(command[2])
        wagons[leaved_index] -= leaved_people


