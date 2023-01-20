# In python a class is an object that has its own attributes
# Class variables are bound to the class. They’re shared by all instances of that class
class Person:
    # class variables
    counter = 0

     # instance variables or instance attributes
    def __init__(self, name, age):
        # the dunder __init__ is not a constructor
        self._name = name # private attributes
        self.__age = age # this attr name is _Person__age
        Person.counter += 1

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age = new_age

    # instance method
    def greet(self):
        return f"Hi, it's {self.name}."

    # class method
    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)
    

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    # special methods

    # the string representation of the instance
    def __str__(self):
        return f'{self._name}'

    def __eq__(self, other):
        return self._name == other._name

    # it uses the object ID by default
    def __hash__(self):
        return hash(self.age)