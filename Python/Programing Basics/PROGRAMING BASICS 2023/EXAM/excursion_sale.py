excursion_sea_count = int(input())
excursion_mountain_count = int(input())

total_price = 0
sea_packet_count = excursion_sea_count
mountain_packet_count = excursion_mountain_count

while True:
    command = input()

    if command == "Stop":
        break

    packet_name = command

    if packet_name == "sea":
        if sea_packet_count == 0:
            continue
        else:
            total_price += 680
            sea_packet_count -= 1

    elif packet_name == "mountain":
        if mountain_packet_count == 0:
            continue
        else:
            total_price += 499
            mountain_packet_count -= 1

    if sea_packet_count == 0 and mountain_packet_count == 0:
        print("Good job! Everything is sold.")
        break

print(f"Profit: {total_price} leva.")