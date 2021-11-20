#Method is to be called when a new object is created
class Human:
    def __init__(self,name): #unlike JS you need to declare self
        #self is the same as this in JavaScript
        #represents and instance of that object
       #this is the body of the constructor
        self.name = name  #name is used to initialize self.name and initialize and create a new property
    def displayName(self):
        print(self.name)

#passing data to classes
employee = Human('Bill')
employee.displayName() # displays Bill