#checkpoint 1 & 2
from Roster import student_roster 
from Classroom_Organiser import ClassroomOrganiser 
import itertools

print("task 1: The full student roster dictionary:")
student_roster_iterator = iter(student_roster)

for i in range(10):
  print(next(student_roster_iterator))

#task 3: Each student by first name, one at a time, alphabetically
print("This is solution to task 2")
new_student = ClassroomOrganiser()
for student in new_student:
  print(student[:-1])

#checkpoint 4 - itertools
print()
print("task 4: all pair combinations of 2 students")
pair_combo_iterator = itertools.combinations(student_roster_iterator, 2)

for combo in pair_combo_iterator:
  print(combo)

#ckeckpoint 5
print()
print("task 5: favorite subject Math:")
print(new_student.get_students_with_subject("Math"))
print()

print("task 5: favorite subject Science:")
print(new_student.get_students_with_subject("Science"))
print()

print("Math & Sceince list of all 4 combinatins of students:")
math_science_list = list(itertools.chain(new_student.get_students_with_subject("Math"), new_student.get_students_with_subject("Science")))
print(math_science_list)
print()

print("task 5: combos of tables of four:")
math_science_fours = list(itertools.combinations(math_science_list, 4))
print(math_science_fours)
