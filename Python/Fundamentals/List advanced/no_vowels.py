text = input()

new_text = [word for word in text if word.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(new_text))