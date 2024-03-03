fruit = input()
day = input()
quanity = float(input())
price = 0
correct_data = True

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = quanity * 2.50
    elif fruit == "apple":
        price = quanity * 1.20
    elif fruit == "orange":
        price = quanity * 0.85
    elif fruit == "grapefruit":
        price = quanity * 1.45
    elif fruit == "kiwi":
        price = quanity * 2.70
    elif fruit == "pineapple":
        price = quanity * 5.50
    elif fruit == "grapes":
        price = quanity * 3.85
    else:
        correct_data = False

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = quanity * 2.70
    elif fruit == "apple":
        price = quanity * 1.25
    elif fruit == "orange":
        price = quanity * 0.90
    elif fruit == "grapefruit":
        price = quanity * 1.60
    elif fruit == "kiwi":
        price = quanity * 3
    elif fruit == "pineapple":
        price = quanity * 5.60
    elif fruit == "grapes":
        price = quanity * 4.20
    else:
        correct_data = False

else:
    correct_data = False

if correct_data:
    print(f"{price:.2f}")
else:
    print("error")