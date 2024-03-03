from math import ceil
from math import floor

magnolias_count = int(input())
zombulius_count = int(input())
roses_count = int(input())
cactuses_count = int(input())
gift_price = float(input())

magnolias_price = 3.25
zombulius_price = 4
roses_price = 3.50
cactuses_price = 8

total_sum = (magnolias_count * magnolias_price) + (zombulius_count * zombulius_price) + \
            (roses_count * roses_price) + (cactuses_count * cactuses_price)

total_sum_with_tax = total_sum * 0.95

if total_sum_with_tax > gift_price:
    print(f"She is left with {floor(total_sum_with_tax - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(abs(total_sum_with_tax - gift_price))} leva.")

