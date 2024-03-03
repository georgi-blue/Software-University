number = int(input())

for i in range(1,number + 1):
    for j in range (0,i):
        print("*",end="")
    print()

for r in range (number - 1, 0,-1):
    for k in range(0,r):
        print("*",end="")
    print()

