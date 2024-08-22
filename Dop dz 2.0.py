students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_s = sorted(students)
print(students_s)

grades_t = []
for new_grades in grades:
    a = sum(new_grades)/len(new_grades)
    grades_t.append(a)
print(grades_t)

grades_student = dict(zip(students_s, grades_t))
print(grades_student)