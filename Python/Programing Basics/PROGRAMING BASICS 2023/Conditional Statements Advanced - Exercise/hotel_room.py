month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights <= 14:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.70

elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio *= 0.80

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if nights > 14:
    apartment *= 0.9

apartment_price = apartment * nights
studio_price = studio * nights

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
