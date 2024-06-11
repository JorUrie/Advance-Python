class Crow:
    # class attribute
    species = 'bird'
    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class name
class MyClass:
    a = 20
    b = 40
# Accessing variable present inside
MyClass
print(MyClass.a)

#Instance the Crow class
blu = Crow('Blu', 10)
woo = Crow('Woo', 15)
# access the class attributes
print('Blu is a {}'.format(blu.__class__.species))
print('Woo is also a {}'.format(woo.__class__.species))
# acces the instance attributes
print('{} is {} years old'.format(blu.name,blu.age))
print('{} is {} years old'.format(woo.name, woo.age))

# Defining Constructor method in a class
class MyClass:
    # default constructor
    def __init__(self):
        self.py = 'Welcome to Python'
    # a method for printing data members
    def print_Py(self):
        print(self.py)
# creating object of the class
obj = MyClass()
# calling the instance method using the object obj
obj.print_Py()

# Inheritance terminologies through an example
# definition of the superclass starts here
class Person:
    # initializing the variables
    name = ''
    age = 0
    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    # defining class methods
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)
    # end of super class definition
# definition if subclass starts here
class Student(Person): # Person is the superclass and Student is the subclass
    studentId = ''
    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName, studentAge) # Calling the superclass constructor and sending values of attributes
        self.studentId = studentId
    def getId(self):
        return self.studentId # returns the value of student id
# end of subclass definition
# Create an abject of the superclass
person1 = Person('John', 23)
# call member methods of the objects
person1.showAge()
# Create an object of the subclass
student1 = Student('Shaun', 22, '102')
print(student1.getId())
student1.showName()

# let's have a hand on an example
# There's a parent class named Animal
class Animal:
    # propieties
    multicellular = True
    # Eukaryotic means Cells with Nucleus
    eukaryotic = True
    # function breathe
    def breathe(self):
        print('I breathe oxygen.')
    # function feed
    def feed(self):
        print('I eat a lot of food')
# Let's create a child class Herbivorous which will extend the class Animal
class Herbivorous(Animal):
    # function feed
    def feed(self):
        print('I eat only plants. I am vegetarian.')
herbi = Herbivorous()
herbi.feed()
# calling some other function
herbi.breathe()
