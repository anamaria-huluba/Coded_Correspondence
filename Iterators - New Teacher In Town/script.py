#checkpoint 1 & 2
from Roster import student_roster 
from Classroom_Organiser import ClassroomOrganiser 
import itertools

print("task 1: The full student roster dictionary:")
student_roster_iterator = iter(student_roster)

for i in range(len(student_roster)):
  print(next(student_roster_iterator))

#task 3: Each student by first name, one at a time, alphabetically
print("This is solution to task 3")
classroom_organiser_iter = iter(ClassroomOrganiser())

for student in classroom_organiser_iter:
  print(student)

#checkpoint 4 - itertools
print()
print("task 4: all pair combinations of 2 students")
print(classroom_organiser_iter.student_pair())

#checkpoint 5
print("task 5: favorite subject Math:")
math_list = classroom_organiser_iter.get_students_with_subject("Math")
print(math_list)
print()
print("task 5: favorite subject Science:")
science_list = classroom_organiser_iter.get_students_with_subject("Science")
print(science_list)
print()
print("task 5: Combined list of students with subjects Math and Science:")
l1 = [math_list + science_list]
combined_list = list(itertools.chain(*l1))
print(combined_list)
print()
print("task 5: combo tables of four:")
print(list(itertools.combinations(combined_list, 4)))
print()

#checkpoint 6
print("task 6: all students of age 7")
seven_list = classroom_organiser_iter.get_student_with_age(7)
print(seven_list)


