trip_price = float(input())
number_puzzles = int(input())
talking_dolls = int(input())
talking_bears = int(input())
minions = int(input())
trucks = int(input())

NUMBER_PUZZLES = 2.6
TALKING_DOLL = 3
TALKING_BEARS = 4.1
MINIONS = 8.2
TRUCKS = 2

total_sum = (number_puzzles * NUMBER_PUZZLES) +\
(talking_dolls * TALKING_DOLL) +\
(talking_bears * TALKING_BEARS) +\
(minions * MINIONS) +\
(trucks * TRUCKS)

number_toys = number_puzzles + talking_dolls + talking_bears + minions + trucks

if number_toys >= 50:
    discount = total_sum / 4
else:
    discount = 0

total_summary_with_discount = total_sum - discount
mortage = total_summary_with_discount * 0.1
profit =  total_summary_with_discount - mortage

if profit >= trip_price:
    money_left = profit - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    needed_money = abs(profit - trip_price)
    print(f"Not enough money! {needed_money:.2f} lv needed.")