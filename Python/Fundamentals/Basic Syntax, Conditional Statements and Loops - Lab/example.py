number = int(input())

for k in range(number + 1,0,-1):
    for j in range(0,k):
        print("*",end=" ")
    print(end=" ")
    print()

for d in range(number+1):
    for s in range(0,d+2):
        print("*",end=" ")
    print(" ")