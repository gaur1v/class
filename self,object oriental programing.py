# class Employ:
#     def hello(self):
#         return f" her name is  {self.name}.he has {self.child} child .he is a {self.work}  "
#
# kirti=Employ()
# manisha=Employ()
# kirti.name="kirti"
# kirti.work="house wife"
# kirti.child=1
# manisha.name="manisha"
# manisha.work="school teacher"
# manisha.child=2
# print(manisha.hello())

class hello:
    def __init__(self,name,salary,role):
        self.sname=name
        self.ssalary=salary
        self.srole=role
    def print(self):
        return f'the name is {self.sname} and the salary is {self.ssalary}. job of {self.srole}'

harry=hello("mohan",'5000','kichan facktery')
print(harry.print())
