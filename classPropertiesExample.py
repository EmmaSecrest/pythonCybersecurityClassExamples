#defining properties -> to get or set the value of an attribute
class Human:
    def __init__(self, name):
        self.name = name
    #used to set data in a more controlled way
    #can set checks here
    @property #similar to a getter in JavaScript
    def name(self):
        return self._name
    @name.setter #similar to a setter in JavaScript
    def name(self,name):
        self._name = name
# with out the underscore you get a recursion error since the method is essentually calling itself


#using the properties
employee = Human('Bill')
print(employee.name)
