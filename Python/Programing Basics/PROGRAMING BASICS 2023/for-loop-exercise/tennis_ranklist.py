from math import floor

participate_tournaments = int(input())
start_points = int(input())

won_tournaments = 0
total_points = 0

for _ in range (participate_tournaments):
    result = input()

    if result == "W":
        total_points += 2000
        won_tournaments += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720

final_points = total_points + start_points
average_points = total_points / participate_tournaments

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{won_tournaments / participate_tournaments * 100:.2f}%")

