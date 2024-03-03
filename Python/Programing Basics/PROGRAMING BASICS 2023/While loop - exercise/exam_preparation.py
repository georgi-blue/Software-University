max_bad_grades = int(input())

total_bad_grades = 0
total_grades = 0
grades_counter = 0
task_counter = 0
last_problem = None

while True:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {total_grades / grades_counter:.2f}")
        print(f"Number of problems: {task_counter}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        total_bad_grades += 1

    grades_counter += 1
    total_grades += grade

    if total_bad_grades == max_bad_grades:
        print(f"You need a break, {total_bad_grades} poor grades.")
        break

    last_problem = task_name
    task_counter += 1
