degrees = int(input())
time_of_the_day = input()

outfit = None
shoes = None

if 10 <= degrees <= 18:
    if time_of_the_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"

    elif time_of_the_day == "Afternoon" or time_of_the_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 < degrees <= 24:
    if time_of_the_day == "Morning" or time_of_the_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

    else:
        outfit = "T-Shirt"
        shoes = "Sandals"

else:
    if time_of_the_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"

    elif time_of_the_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"

    else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")