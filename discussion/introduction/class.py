'''Construct a class hierarchy for people on a college campus. 
Include faculty, staff, and students. What do they have in common? 
What distinguishes them from one another?'''

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name

class Student(Person):

	def __init__(self, name, age, student_id, major):
		Person.__init__(self, name, age)

		self.id = id
		self.major = major

class Employee(Person):

	def __init__(self, name, age, employee_id, salary):
		Person.__init__(self, name, age)

		self.employee_id = employee_id
		self.salary = salary

class Undergrad(Student):

	def __init__(self, name, age, student_id, major):
		Student.__init__(self, name, age, student_id, major)

class Grad(Student):

	def __init__(self, name, age, student_id, major):
		Student.__init__(self, name, age, student_id, major)

class Staff(Employee):

	def __init__(self, name, age, employee_id, salary):
		Employee.__init__(self, name, age, employee_id, salary)

class Faculty(Employee):

	def __init__(self, name, age, employee_id, salary):
		Employee.__init__(self, name, age, employee_id, salary)


bob = Undergrad("Bob", 19, "b123", 'CS')
jerry = Faculty("Jerry", 45, "j123", 60)	

print(bob)
print(jerry)	


