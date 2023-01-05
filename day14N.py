class Complex:
    def  __init__(self,real,img):
        self.real=real
        self.img=img
    def __sub__(self,ob):
       temp=self.real-ob.real,ob.real-ob.img
       return temp
    def __str__(self):
         return (self.real,self.img)
ob1=Complex(3,5)
ob2=Complex(2,19)
ob3=ob1-ob2
print(ob3)



'''output:
==========    
(1, -17)'''
