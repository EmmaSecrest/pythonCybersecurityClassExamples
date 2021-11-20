#class Methods can be shared by all instances of that class
class User:
    numVisitors = 0
    def __init__(self, name):
        self.name = name
        User.numVisitors += 1
    @classmethod
    def displayNumVisitors(cls):
        print("numVisitors: " , User.numVisitors)


jane =User("Jane")
User.displayNumVisitors() # displays numVisitor: 1
john = User("John")
User.displayNumVisitors() #displays numVisitor: 2
