pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input()) / 100

PAN_PRICE = 5.8
MARKERS_PRICE = 7.2
DETERGENT_PRICE = 1.2

price_before_discount = (pens * PAN_PRICE) + (markers * MARKERS_PRICE) + (detergent * DETERGENT_PRICE)
total_price = price_before_discount -  price_before_discount * discount


print(total_price)