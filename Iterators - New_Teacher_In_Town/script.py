#checkpoint 1 & 2
from Roster import student_roster 
from Classroom_Organiser import ClassroomOrganiser 
import itertools

print("This is solution to task 1")
print("The full student roster (dictionary):")
student_roster_iterator = iter(student_roster)

print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))
print(next(student_roster_iterator))

#checkpoint 3: Each student by first name, one at a time, alphabetically
print("This is solution to task 2")
new_student = ClassroomOrganiser()
for student in new_student:
  print(student[:-1])

#checkpoint 4 - itertools
print()
print("This is solution to task 4")
pair_combo_iterator = itertools.combinations(student_roster_iterator, 2)

for combo in pair_combo_iterator:
  print(combo)

print(new_student.get_students_with_subject("Math"))
print(new_student.get_students_with_subject("Science"))
print()

#ckeckpoint 5
print("task 5: favorite subject is Math or Science")
math_science_list = list(itertools.chain(new_student.get_students_with_subject("Math"), new_student.get_students_with_subject("Science")))
print(math_science_list)
print()
print("task 5: combos of tables of four.")
math_science_fours = list(itertools.combinations(math_science_list, 4))
print(math_science_fours)