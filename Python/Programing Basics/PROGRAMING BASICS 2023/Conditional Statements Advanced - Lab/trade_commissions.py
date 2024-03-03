city = input()
volume_sales = float(input())
comission = 0
correct_data = True

if city == "Sofia":
    if 0 <= volume_sales <= 500:
        comission = volume_sales * 0.05
    elif 500 < volume_sales <= 1000:
        comission = volume_sales * 0.07
    elif 1000 < volume_sales <= 10000:
        comission = volume_sales * 0.08
    elif volume_sales > 10000:
        comission = volume_sales * 0.12
    else:
        correct_data = False

elif city == "Varna":
    if 0 <= volume_sales <= 500:
        comission = volume_sales * 0.045
    elif 500 < volume_sales <= 1000:
        comission = volume_sales * 0.075
    elif 1000 < volume_sales <= 10000:
        comission = volume_sales * 0.10
    elif volume_sales > 10000:
        comission = volume_sales * 0.13
    else:
        correct_data = False

elif city == "Plovdiv":
    if 0 <= volume_sales <= 500:
        comission = volume_sales * 0.055
    elif 500 < volume_sales <= 1000:
        comission = volume_sales * 0.08
    elif 1000 < volume_sales <= 10000:
        comission = volume_sales * 0.12
    elif volume_sales > 10000:
        comission = volume_sales * 0.145
    else:
        correct_data = False

else:
    correct_data = False

if correct_data:
    print(f"{comission:.2f}")
else:
    print("error")