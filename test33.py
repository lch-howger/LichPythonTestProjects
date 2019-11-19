class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print('Hello, my name is {}, I am {}.'.format(self.name, self.age))


stu = Student('Abc', 20)
stu.sayhi()


class LocalStudent(Student):
    def __init__(self, name, age):
        Student.__init__(self,name,age)

    def sayhi(self):
        Student.sayhi()


local = LocalStudent('name',32)
local.sayhi()
