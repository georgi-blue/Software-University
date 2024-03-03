text = input().split()


new_word = ""

for word in text:
    lenght = len(word)
    new_word += word * lenght

print(new_word)