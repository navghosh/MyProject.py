#code for constructor

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap=self.laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()


    class laptop:

        def __init__(self):
            self.brand="apple"
            self.cpu="iOs"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student("navneet", 22)
s2=Student("nitin", 21)

s1.show()
s2.show()

lap=Student.laptop()