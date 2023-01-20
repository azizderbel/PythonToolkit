class Employee:

    def __init__(self,first_name,last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        #self.email = self.first_name + '.' + self.last_name + '@gmail.com'
    
    @property
    def email(self):
        return self.first_name + '.' + self.last_name + '@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)

    @fullname.setter
    def fullname(self,fullname):
        self.first_name,self.last_name = fullname.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None

    

emp1 = Employee('Corey','shafer')
print(emp1.email)
emp1.fullname = 'Aziz derbel'
print(emp1.fullname)
print(emp1.email)

