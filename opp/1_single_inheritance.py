
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    # overrride the greet function
    def greet(self):
        return super().greet() + ''
