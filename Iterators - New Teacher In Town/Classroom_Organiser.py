from Roster import student_roster 
import itertools 

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)
    self.index = 0
    self.student_roster = student_roster

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    next_student = self.sorted_names[self.index]
    self.index += 1
    if self.index >= len(self.sorted_names):
      raise StopIteration
    return next_student 
  
  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      #to only output first name without the surename Initial:
      first_name = name.split()
      names.append(first_name)
    return sorted(names)
  
  def student_pair(self):
    return list(itertools.combinations(self.sorted_names, 2))

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def get_student_with_age(self, age):
    selected_students = []
    for student in student_roster:
      if student['age'] == age:
        selected_students.append((student['name'], age))
    return selected_students
    