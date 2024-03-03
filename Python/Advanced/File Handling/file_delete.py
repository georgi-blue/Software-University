import os

path = os.path.join("my_first_file")


try:
    os.remove(path)
except FileNotFoundError:
    print("File already deleted")


if os.path.exists(path):
    os.remove(path)
else:
    print("File is already deleted ")