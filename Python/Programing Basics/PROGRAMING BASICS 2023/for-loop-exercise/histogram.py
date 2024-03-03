numbers = int(input())

p1,p2,p3,p4,p5 = 0, 0, 0, 0, 0


for _ in range (numbers):
    single_number = int(input())

    if single_number < 200:
        p1 += 1
    elif single_number < 400:
        p2 += 1
    elif single_number < 600:
        p3 += 1
    elif single_number < 800:
        p4 += 1
    else:
        p5 += 1

print(f"{p1 / numbers * 100:.2f}%")
print(f"{p2 / numbers * 100:.2f}%")
print(f"{p3 / numbers * 100:.2f}%")
print(f"{p4 / numbers * 100:.2f}%")
print(f"{p5 / numbers * 100:.2f}%")