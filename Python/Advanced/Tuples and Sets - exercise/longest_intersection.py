longest_intersection_numbers = set()


for _ in range(int(input())):
    first_data, second_data = [num.split(",") for num in input().split("-")]

    first_set = set(range(int(first_data[0]),  int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection_numbers):
        longest_intersection_numbers = intersection

print(f"Longest intersection is "
    f"[{', '.join(str(x) for x in longest_intersection_numbers)}] "
    f"with length {len(longest_intersection_numbers)}")