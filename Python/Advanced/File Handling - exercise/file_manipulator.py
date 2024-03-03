import os

while True:
    command, *files = input().split("-")

    if command == "Create":
        with open(f"{files[0]}", "w"): pass

    elif command == "Add":
        try:
            with open(f"{files[0]}", "a") as file:
                file.write(f"\n{files[1]}")

        except FileNotFoundError:
            with open(f"{files[0]}", "a"): pass

    elif command == "Replace":
        try:
            with open(f"{files[0]}", "r+") as file:
                text = file.read()
                text = text.replace(files[1],files[2])


                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove(f"{files[0]}")
        except FileNotFoundError:
            print("An error occurred")

    elif command == "End":
        break