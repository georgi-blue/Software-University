lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = lenght * width * height
volume_liters = aquarium_volume / 1000
busy_space = percent / 100
needed_space = volume_liters * (1-busy_space)

print(needed_space)