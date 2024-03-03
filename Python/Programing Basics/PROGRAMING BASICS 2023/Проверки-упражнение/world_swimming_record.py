from math import floor

time_seconds = float(input())
time_meters = float(input())
time_seconds_one_meter = float(input())

total_seconds = time_meters * time_seconds_one_meter
reverse = floor(time_meters / 15) * 12.5
total_time = total_seconds + reverse

if time_seconds < total_time:
    needed_time = abs(time_seconds - total_time)
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")

if time_seconds >= total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

