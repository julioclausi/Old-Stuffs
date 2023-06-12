my_student_class = {}

while True:
    student = input('Name of student: ')
    if student == 'quit':
        break
    grade_1 = int(input('Grade 1: '))
    grade_2 = int(input('Grade 2: '))
    grade_3 = int(input('Grade 3: '))
    grade_4 = int(input('Grade 4: '))
    avg_grade = (grade_1 + grade_2 + grade_3 + grade_4) / 4
    print (f'Student {student} -> avg {avg_grade}')
    my_student_class.update({student:avg_grade})

print (my_student_class)