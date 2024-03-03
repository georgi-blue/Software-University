travel_route = input().split("||")
starting_fuel = int(input())
starting_amunnition = int(input())

for each in travel_route:
    each = each.split()
    command = each[0]
    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        value = each[1]
    if command == "Travel":
        consume_fuel = int(value)

        if starting_fuel >= consume_fuel:
            starting_fuel -= consume_fuel
            print(f"The spaceship travelled {consume_fuel} light-years.")
        else:
            print("Mission failed. ")
            break

    elif command == "Enemy":
        enemy_armor = int(value)

        if starting_amunnition >= enemy_armor:
            starting_amunnition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")


        elif starting_fuel >= enemy_armor:
            starting_fuel -= enemy_armor * 2
            print(f"An enemy with {enemy_armor} armour is outmaneuvered.")

        else:
            print("Mission failed. ")
            break

    elif command == "Repair":
        benefits = int(value)
        starting_fuel += benefits
        starting_amunnition += benefits * 2
        print(f"Ammunitions added: {benefits * 2}.")
        print(f"Fuel added: {benefits}.")