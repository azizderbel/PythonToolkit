# instance methods take the instance as first argument 'self'
# class methods take the class as the first argument 'cls
# static methids do not pass anything automatically
class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self,first_name,last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    # alternative initializer
    def from_string(cls,emp_str):
        first_name,last_name = emp_str.split('-')
        return cls(first_name=first_name,last_name=last_name)

    @staticmethod
    def is_workday(day):
        pass


Employee.set_raise_amt(1.05)

emp1 = Employee('Corey','shafer')
emp2 = Employee('Terb','Hikol')
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
emp3 = Employee.from_string('aziz-derbel')
print(emp3.first_name)
