students_number = int(input())
total_lectures = int(input())
additional_bonus = int(input())

bonus_list = []
student_list = []

for student in range(students_number):
    count_attendances_student = int(input())
    student_list.append(count_attendances_student)

    total_bonus = round((count_attendances_student / total_lectures) * (5 + additional_bonus))
    bonus_list.append(total_bonus)


print(f"Max Bonus: {max(bonus_list)}.")
print(f"The student has attended {max(student_list)} lectures.")





