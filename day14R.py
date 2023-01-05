class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1
    def displayCount(self):
        print("Total Employee:%d" %Employee.empCount)
    def displayEmployee(self):
         print("Name :",self.name,",salary: ",self.salary)
emp1=Employee("jyothsnarani",99900)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))#RETURN   VALUES   OF 'SALARY' ATTRIBUTE
setattr(emp1,'salary',10000)#SET   ATTRIBUTE    '  SALARY'   AT   10000
print("Modified salary ",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg',',anager')
print(hasattr(emp1,'desg'))
print("Added A ttribute",getattr(emp1,'desg'))
delattr(emp1,'salary')#DELETE ATTRIBUTE 'SALARY'
print("is salary an attribute:",hasattr(emp1,'salary'))



 
'''OUTPUT:
==================
    
Name : jyothsnarani ,salary:  99900
is salary an attribute: True
99900
Modified salary  10000
False
True
Added A ttribute ,anager
is salary an attribute: False'''
