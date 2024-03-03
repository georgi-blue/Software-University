string = input()
command = input()

while command != "Complete":
    if command == "Make Upper":
        string = string.upper()
        print(string)
    elif command == "Make Lower":
        string = string.lower()
        print(string)
    elif command.startswith("GetDomain"):
        none, count = command.split()
        count = int(count)
        domain = string[-count:]
        print(domain)
    elif command == "GetUsername":
        if "@" in string:
            username = string.split("@")[0]
        else:
            username = (f"The email {string} doesn't contain the @ symbol.")
        print(username)
    elif command.startswith("Replace"):
        char = command.split()[1]
        string = string.replace(char, '-')
        print(string)
    elif command == "Encrypt":
        result = " ".join(str(ord(char)) for char in string)
        print(result)
    command = input()