parking = set()


for _ in range(int(input())):
    direction,car_plate = input().split(", ")

    if direction == "IN":
        parking.add(car_plate)

    elif direction == "OUT":
        parking.remove(car_plate)



if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")