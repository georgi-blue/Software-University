w = float(input())
h = float(input())

number_of_seats_per_width = int(w / 1.20)
number_of_seats_per_lenght = int((h - 1) / 0.70)
number_of_seats_in_room = number_of_seats_per_width * number_of_seats_per_lenght - 3

print(int(number_of_seats_in_room))
