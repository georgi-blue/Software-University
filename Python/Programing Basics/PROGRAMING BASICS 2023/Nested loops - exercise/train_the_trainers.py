judges_count = int(input())

sum_grades = 0
total_grades = 0


while True:
    presentation = input()

    if presentation == "Finish":
        break

    grades_sum = 0

    for _ in range(judges_count):
        grades_sum += float(input())


    sum_grades += grades_sum
    total_grades += judges_count

    print(f"{presentation} - {grades_sum / judges_count:.2f}.")

print(f"Student's final assessment is {sum_grades / total_grades:.2f}.")



