n_tabs_open = int(input())
salary = int(input())

for _ in range (n_tabs_open):
    tabs = input()

    if tabs == "Facebook":
        salary -= 150
    elif tabs == "Instagram":
        salary -= 100
    elif tabs == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        break

else:
    print(salary)