K = int(input())
L = int(input())
M = int(input())
N = int(input())

count = 0
data = False

for i in range(K, 9):
    for j in range(9, L + 1, - 1):
        for k in range(M, 9):
            for l in range(9, N + 1, - 1):
                if i % 2 == 0 and j % 2 == 1 and k % 2 == 0 and l % 2 == 1:
                    if i != k or j != l:
                        print(f"{i}{j} - {k}{l}")
                        count += 1
                        if count == 6:
                            data = True
                            break
                    else:
                        print("Cannot change the same player.")

    if data:
        break