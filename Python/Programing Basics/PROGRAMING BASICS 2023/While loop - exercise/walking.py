GOAL = 10_000
total_steps = 0


while total_steps < GOAL:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        total_steps += steps
        break

    else:
        actually_steps = int(steps)
        total_steps += actually_steps

if GOAL > total_steps:
    print(f"{GOAL - total_steps} more steps to reach goal.")

else:
    print("Goal reached! Good job!")
    print(f"{total_steps - GOAL} steps over the goal!")