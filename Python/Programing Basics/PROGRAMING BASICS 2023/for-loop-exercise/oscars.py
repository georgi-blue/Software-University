actor_name = input()
start_points = float(input())
judges = int(input())

total_points = 0

for _ in range (judges):
    judge_name = input()
    judge_points = float(input())

    total_points += (len(judge_name) * judge_points) / 2

    if total_points + start_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points + start_points:.1f}!")
        break
else:
        print(f"Sorry, {actor_name} you need {abs((total_points + start_points) - 1250.5):.1f} more!")