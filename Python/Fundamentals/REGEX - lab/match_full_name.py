import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
match = re.findall(pattern, text)

print(' '.join(match))