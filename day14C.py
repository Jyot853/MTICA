class Wolf:
    price=500
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Gur...")
class Dog(Wolf):
        def bark1(self):
            print("Woof")

class Dog(Wolf):
    def bark1(self):
        print("Woof")
if __name__=="__main__":
    pet1=Dog("Tomy","brown")
    pet1.bark()
    pet1.bark1()
    print(pet1.name,"is of colour",pet1.color)


output:

==========================
Gur...
Woof
Tomy is of colour brown
