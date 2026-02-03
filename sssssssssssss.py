student_one ={'name':'ahmed','grades': [30, 60, 70] }
student_two ={'name':'noor', 'grades': [50, 70, 60]}
student_three ={'name':'nada', 'grades': [70, 80, 50]}
for student in student_one , student_two ,student_three:
    average = sum(student['grades']) / len(student['grades'])
    print(f'student: {student['name']}')
    print(f'grades: {student['grades']}')
    print(f'average: {average:.2f}')

