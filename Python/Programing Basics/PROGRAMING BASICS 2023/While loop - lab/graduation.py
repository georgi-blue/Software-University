student_name = input()

failed_counter = 0
years_in_school_counter = 0
year_grade = 0
sum_grades = 0

while years_in_school_counter < 12:
    grade = float(input())
    if grade >= 4:
        years_in_school_counter += 1
        sum_grades += grade
        year_grade += 1
        if years_in_school_counter == 12:
            print(f"{student_name} graduated. Average grade: {sum_grades / 12:.2f}")
            break

    else:
        failed_counter += 1


    if failed_counter > 1:
        print(f"{student_name} has been excluded at {year_grade + 1} grade")
        break

