n1 = int(input())
n2 = int(input())


for number in range (n1, n2 + 1):
    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(str(number)):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if odd_sum == even_sum:
        print(number, end=" ")




