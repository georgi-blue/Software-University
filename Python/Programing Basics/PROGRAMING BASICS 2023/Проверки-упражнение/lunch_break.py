from math import ceil

series_name = str(input())
episode_lenght = int(input())
break_time = int(input())

lunch_time = ceil(break_time * 1/8)
free_time = ceil(break_time * 1/4)
time_left = ceil(break_time - lunch_time - free_time)

if time_left >= episode_lenght:
    extra_time = ceil(time_left - episode_lenght)
    print(f"You have enough time to watch {series_name} and left with {ceil(extra_time)} minutes free time.")
elif time_left < episode_lenght:
    time_needed = ceil(abs(time_left - episode_lenght))
    print(f"You don't have enough time to watch {series_name}, you need {ceil(time_needed)} more minutes.")