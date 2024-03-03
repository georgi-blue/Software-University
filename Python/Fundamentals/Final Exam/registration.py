import re

input_count = int(input())
valid_registrations = 0
pattern = r"^U\$([A-Z][a-z]{2,})U\$P@\$(?=[A-Za-z]{5,}\d+)(.*\d+)P@\$"

for i in range(input_count):
    user_info = input()
    match = re.match(pattern, user_info)

    if match:
        username = match.group(1)
        password = match.group(2)
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")
        valid_registrations += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {valid_registrations}")

