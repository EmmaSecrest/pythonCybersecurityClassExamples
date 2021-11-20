# inheritance is recyling old code and reusing it
class Human:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

#employee reuses some of the code from human to make it much easier to create the class Employee
class Employee(Human):
    def __init__(self,name,title):
        Human.__init__(self,name)
        self._title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        self._title = title

employee = Employee('Bill','CEO')
print(employee.title , employee.name) #displays CEO Bill