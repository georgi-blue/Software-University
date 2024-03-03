from collections import deque

day_food = int(input())

orders = deque(input().split())


while orders:
    current_order = [int(order) for order in orders]
    for food in current_order:
        if day_food >= food:
            orders.popleft()
            day_food -= food
        else:
            break
    break

print(max(current_order))

if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")

