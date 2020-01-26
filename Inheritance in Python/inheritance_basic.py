# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person: 
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  
  def PrintName(self):
    print(self.firstname, self.lastname)


newPersion = Person('Hasan', 'Mahmud')
print(newPersion.PrintName())