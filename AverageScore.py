grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

student_and_average_score = {}

Aaron_score = sum(grades[0]) / len(grades[0])
Bilbo_score = sum(grades[1]) / len(grades[1])
Johnny_score = sum(grades[2]) / len(grades[2])
Khendrik_score = sum(grades[3]) / len(grades[3])
Steve_score = sum(grades[4]) / len(grades[4])

student_and_average_score['Aaron'] = Aaron_score
student_and_average_score['Bilbo'] = Bilbo_score
student_and_average_score['Johnny'] = Johnny_score
student_and_average_score['Khendrik'] = Khendrik_score
student_and_average_score['Steve'] = Steve_score




print(student_and_average_score)


