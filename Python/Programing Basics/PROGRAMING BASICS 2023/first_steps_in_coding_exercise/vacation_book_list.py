pages = int(input())
pages_per_hour = int(input())
days_for_book = int(input())

total_time_needed = pages // pages_per_hour
total_hours_per_day = total_time_needed // days_for_book

print(total_hours_per_day)