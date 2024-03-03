prime_sum = 0
non_prime_sum = 0

while True:
    command = input()

    if command == "stop":
        break

    number = int(command)

    if number < 0:
        print("Number is negative.")
        continue

    for n in range(2, number):
        if number % n == 0:
            break
    else:
        prime_sum += number
        continue

    non_prime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")



