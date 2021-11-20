# declared at a class scope can be shared by all instances of that class
class User:
   numVisitors = 0 #class variable initialized
   #associated with the class as a whole
   def __init__(self, name):
       self.name = name #instance initialized
       User.numVisitors += 1 #class variable Updated

sally = User('Sally')
print("User.Name: " , sally.name, "\tUser.numVisitors: ", User.numVisitors)

joe = User('Joe')
print("User.Name: " , joe.name, "\tUser.numVisitors: ", User.numVisitors)

print("User.Name: " , sally.name, "\tUser.numVisitors: ", User.numVisitors)