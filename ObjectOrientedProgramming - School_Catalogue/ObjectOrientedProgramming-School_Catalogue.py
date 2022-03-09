
class School():

  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def getname(self):
    return self.name
  
  def getlevel(self):
    return self.level
  
  def getnumberOfStudents(self):
    return self.numberOfStudents
  
  def setnumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents 
  
  def __repr__(self):
    return("A {} school name {} with {} students".format(self.level, self.name, self.numberOfStudents))

mySchool = School("Codecademy", "high", 100)
print(mySchool)
print(mySchool.getname())
print(mySchool.getlevel())
mySchool.setnumberOfStudents(200)
print(mySchool.getnumberOfStudents())

Output:
A high school name Codecademy with 100 students
Codecademy
high
200

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def getpickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup polity is {}".format(self.pickupPolicy)

testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.getpickupPolicy())
print(testSchool)

Outputs:
Pickup Allowed
A primary school name Codecademy with 300 students The pickup polity is Pickup Allowed

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams
    
  def getsportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " and with {} Sports Teams".format(self.sportsTeams)

otherSchool = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(otherSchool.getsportsTeams())
print(otherSchool)

Outputs:
['Tennis', 'Basketball']
A high school name Codecademy High with 500 students and with ['Tennis', 'Basketball'] Sports Teams
