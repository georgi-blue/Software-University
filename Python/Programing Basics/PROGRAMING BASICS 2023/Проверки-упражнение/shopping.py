petur_budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())


GPU_PRICE = 250
CPU_PRICE = (gpu_count * GPU_PRICE) * 0.35
RAM_PRICE = (gpu_count * GPU_PRICE) / 10

price_summary = (ram_count * RAM_PRICE) + (gpu_count * GPU_PRICE) + (cpu_count * CPU_PRICE)

if gpu_count > cpu_count:
    discount = price_summary * 0.15
else:
    discount = 0


total_summary = price_summary - discount


if total_summary > petur_budget:
    needed_money = abs(total_summary - petur_budget)
    print(f"Not enough money! You need {needed_money:.2f} leva more!")

if total_summary <= petur_budget:
    money_left = petur_budget - total_summary
    print(f"You have {money_left:.2f} leva left!")