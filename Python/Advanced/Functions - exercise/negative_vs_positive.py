def nums(numbers):
    positive_sum = sum(n for n in numbers if n > 0)
    negative_sum = sum(n for n in numbers if n < 0)

    print(negative_sum)
    print(positive_sum)

    if positive_sum > abs(negative_sum):
        print(f"The positives are stronger than the negatives")
    elif abs(negative_sum) > positive_sum:
        print(f"The negatives are stronger than the positives")

numbers = [int(x) for x in input().split()]

nums(numbers)