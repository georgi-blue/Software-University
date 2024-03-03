from collections import deque

clothes = deque(input().split())

one_rack_capacity = int(input())

racks_counter = 1
current_capacity = one_rack_capacity

while clothes:
    current_cloth = int(clothes.pop())

    if current_cloth <= current_capacity:
        current_capacity -= current_cloth

    else:
        racks_counter += 1
        current_capacity = one_rack_capacity - current_cloth

print(f"{racks_counter}")