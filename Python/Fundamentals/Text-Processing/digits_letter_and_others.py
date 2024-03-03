text = input()

digits_found = ""
letters_found = ""
characters_found = ""

for ch in text:
    if ch.isdigit():
        digits_found += ch
    elif ch.isalpha():
        letters_found += ch

    else:
        characters_found += ch

print(digits_found)
print(letters_found)
print(characters_found)