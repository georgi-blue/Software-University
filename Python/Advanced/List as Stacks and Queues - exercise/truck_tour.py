from collections import deque

gas_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])  # [[1, 5], [10, 3], [1, 3]]

gas_data_copy = gas_data.copy()
petrol_in_tank = 0
index = 0

while gas_data_copy:
    petrol, distance = gas_data_copy.popleft()

    petrol_in_tank += petrol

    if petrol_in_tank >= distance:
        petrol_in_tank -= distance
    else:
        gas_data.rotate(-1)
        pumps_data_copy = gas_data.copy()
        index += 1
        gas_in_tank = 0

print(index)