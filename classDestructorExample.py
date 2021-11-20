#destructor is invoked when an instance is being destroyed
class User:
    def __init__(self,name):
        self.name = name
        print(self.name, 'Created')
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    def __del__(self):
        print(self.name , "Destroyed")

admin = User('Admin') #user Created
del admin  # user Destroyed