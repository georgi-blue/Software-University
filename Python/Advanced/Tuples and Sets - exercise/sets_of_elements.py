lenght1,lenght2 = [int(x) for x in input().split()]

first_set = set([input() for _ in range(lenght1)])
second_set = set(input() for _ in range(lenght2))


print(*first_set.intersection(second_set), sep='\n')