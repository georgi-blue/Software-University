shirt_price = float(input())
ball_price_to_reach = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (shirt_price + shorts_price) * 2

total_sum = shirt_price + shorts_price + socks_price + shoes_price
total_sum_with_discount = total_sum * 0.85

if total_sum_with_discount >= ball_price_to_reach:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_with_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {ball_price_to_reach - total_sum_with_discount:.2f} lv. more.")