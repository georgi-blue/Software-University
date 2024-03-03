days_rent = int(input()) - 1
room_kind = input()
degree = input()

value = 0


if room_kind == "room for one person":
    value = days_rent * 18

elif room_kind == "apartment":
    value = days_rent * 25
    if days_rent < 10:
        value *= 0.70
    elif 10 <= days_rent <= 15:
        value *= 0.65
    elif days_rent > 15:
        value *= 0.50

elif room_kind == "president apartment":
    value = days_rent * 35
    if days_rent < 10:
        value *= 0.90
    elif 10 <= days_rent <= 15:
        value *= 0.85
    elif days_rent > 15:
        value *= 0.80
if degree == "positive":
    value += value * 0.25
elif degree == "negative":
  value -= value * 0.1

print(f"{value:.2f}")
