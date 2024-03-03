N1 = int(input())
N2 = int(input())
operator = input()

result = ""

if operator == "+":
    result = f"{N1} + {N2} = {N1 + N2}" + (" - even" if (N1 + N2) % 2 == 0 else " - odd")
elif operator == "-":
    result = f"{N1} - {N2} = {N1 - N2}" + (" - even" if (N1 - N2) % 2 == 0 else " - odd")
elif operator == "*":
    result = f"{N1} * {N2} = {N1 * N2}" + (" - even" if (N1 * N2) % 2 == 0 else " - odd")
elif N2 == 0:
    result = f"Cannot divide {N1} by zero"
elif operator == "/":
    result = f"{N1} / {N2} = {N1 / N2:.2f}"
elif operator == "%":
    result = f"{N1} % {N2} = {N1 % N2}"

print(result)

