class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1
    def displayCount(self):
        print("Total Employee:{0}" .format(Employee.empCount))
    def displayEmployee(self):
        print("Name:    ",self .name,    ",  salary:   " ,self.salary)
emp1=Employee("Jyothsna",99000)
emp1.displayEmployee()
emp1.salary=10000
emp1.experience=4
emp1.displayEmployee()
emp1.name='Manoj'
emp1.displayEmployee()
print(emp1.experience)
#del emp1.salary
emp1.displayEmployee()


'''OUTPUT:

===================
Name:     Jyothsna ,  salary:    99000
Name:     Jyothsna ,  salary:    10000
Name:     Manoj ,  salary:    10000
4
Name:     Manoj ,  salary:    10000'''
