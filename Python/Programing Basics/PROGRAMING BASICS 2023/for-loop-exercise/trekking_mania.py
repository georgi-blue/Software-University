groups = int(input())

Musala = 0
Monblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0

for _ in range (groups):
    group_members = int(input())

    if group_members < 6:
        Musala += group_members
    elif group_members < 13:
        Monblan += group_members
    elif group_members < 26:
        Kilimandjaro += group_members
    elif group_members < 41:
        K2 += group_members
    elif group_members >= 41:
        Everest += group_members

total_people = Monblan + Musala + Kilimandjaro + K2 + Everest

print(f"{Musala / total_people * 100:.2f}%")
print(f"{Monblan / total_people * 100:.2f}%")
print(f"{Kilimandjaro / total_people * 100:.2f}%")
print(f"{K2 / total_people * 100:.2f}%")
print(f"{Everest / total_people * 100:.2f}%")
