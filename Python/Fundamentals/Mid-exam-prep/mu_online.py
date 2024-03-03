dungeon_room = input().split("|")

health = 100
bitcoin = 0
best_room = 0

for room in dungeon_room:
    splitter = room.split()
    command = splitter[0]
    number_action = int(splitter[1])
    best_room += 1

    if command == "potion":
        short_health = health
        health += number_action
        if health > 100:
            health = 100
        difference = health - short_health
        print(f"You healed for {difference} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoin += number_action
        print(f"You found {number_action} bitcoins.")

    else:
        health -= number_action
        if health > 0:
            print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break


if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")