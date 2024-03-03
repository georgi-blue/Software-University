CPU_price = float(input()) * 1.57
GPU_price = float(input()) * 1.57
RAM_price = float(input()) * 1.57
RAM_count = int(input())
discount = float(input())

total_RAM = RAM_count * RAM_price
cpu_total_price = CPU_price - (CPU_price * discount)
gpu_total_price = GPU_price - (GPU_price * discount)

total_price = cpu_total_price + gpu_total_price + total_RAM
print(f"Money needed - {total_price:.2f} leva.")