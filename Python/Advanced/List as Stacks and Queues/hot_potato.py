from collections import deque


names = deque(input().split())
tons = int(input()) - 1

while len(names) > 1:
    names.rotate(-tons)
    burned_name = names.popleft()
    print(f"Removed {burned_name}")

print(f"Last is {names.popleft()}")