class Person:
    def sayhi(self):
        print('hello')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getname(self):
        print('Name: {}'.format(self.name))


class Student(Person):
    def stuhi(self):
        print('student')

    def __init__(self, name, age):
        Person.__init__(self, name, age)


class Teacher(Person):
    def teahi(self):
        print('teahcer')


stu = Student('abc',20)

stu.sayhi()
stu.stuhi()
stu.getname()
