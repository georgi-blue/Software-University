needed_exp = float(input())
count_of_battles = int(input())

total_exp = 0
battle_count = 0

for battle in range(1, count_of_battles + 1):
    exp_per_battle = float(input())

    if battle % 3 == 0:
        exp_per_battle *= 1.15

    if battle % 5 == 0:
        exp_per_battle *= 0.9

    if battle % 15 == 0:
        exp_per_battle *= 1.05

    battle_count += 1
    total_exp += exp_per_battle

    if total_exp >= needed_exp:
        break

if total_exp >= needed_exp:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_exp - total_exp:.2f} more needed.")


