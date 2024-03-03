number_of_floors = int(input())
flats_per_floor = int(input())

flat_name = ""

for current_floor in range(number_of_floors, 0, -1):
    for n in range (flats_per_floor):

        if current_floor == number_of_floors:
            flat_name = f"L{current_floor}{n}"

        elif current_floor % 2 == 0:
            flat_name = f"O{current_floor}{n}"

        elif current_floor != 0:
            flat_name = f"A{current_floor}{n}"

        print(flat_name, end=" ")

    print()