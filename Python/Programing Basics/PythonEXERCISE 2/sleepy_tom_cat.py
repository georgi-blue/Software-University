rest_days = int(input())
difference = 0
hours = 0
minutes = 0

YEAR = 365
WORK_DAYS_PLAY = 63
REST_DAYS_PLAY = 127
NORMAL_PLAY = 30000

total_play_rest_days = rest_days * REST_DAYS_PLAY
total_work_days = YEAR - rest_days
total_play_work_days = total_work_days * WORK_DAYS_PLAY
total_play = total_play_work_days + total_play_rest_days

if NORMAL_PLAY < total_play:
   difference = abs(NORMAL_PLAY - total_play)
   hours = difference // 60
   minutes = difference % 60
   print("Tom will run away")
   print(f"{hours} hours and {minutes} minutes more for play")
elif NORMAL_PLAY > total_play:
    difference = (NORMAL_PLAY - total_play)
    hours = difference // 60
    minutes = difference % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
