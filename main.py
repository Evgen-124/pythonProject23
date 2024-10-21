grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(list(students))
student_averages = {}
for i in range(len(sorted_students)):
    student = sorted_students[i]
    student_grades = grades[i]
    average_grade = sum(student_grades) / len(student_grades)
    student_averages[student] = average_grade
print(student_averages)