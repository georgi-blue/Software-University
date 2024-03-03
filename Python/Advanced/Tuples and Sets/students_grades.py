
student_grades = {}

for _ in range(int(input())):
    name,current_grade = input().split()

    if name not in student_grades.keys():
        student_grades[name] = list()
        student_grades[name].append(float(current_grade))
    else:
        student_grades[name].append(float(current_grade))


for student,grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    formatted_grade = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{student} -> {formatted_grade} (avg: {average_grade:.2f})")


