budget = float(input())
season = input()

destination = None
camp_or_hotel = None

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        camp_or_hotel = "Camp"
        budget *= 0.30

    elif season == "winter":
        camp_or_hotel = "Hotel"
        budget *= 0.70

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        camp_or_hotel = "Camp"
        budget *= 0.40

    elif season == "winter":
        camp_or_hotel = "Hotel"
        budget *= 0.80

else:
    destination = "Europe"
    camp_or_hotel = "Hotel"
    budget *= 0.90

print(f"Somewhere in {destination}")
print(f"{camp_or_hotel} - {budget:.2f}")

