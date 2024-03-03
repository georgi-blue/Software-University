text = input()

while True:

    if text.lower() == "end":
        break

    new_text = text[::-1]
    print(f"{text} = {new_text}")
    text = input()
