class Vechicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vechicle):
    pass
school_bus=Bus("school volvo",180,12)
print("Vechicle Name:",school_bus.name,"Speed:",
          school_bus.max_speed,"Milege:",school_bus.mileage)
    

'''output:
=========
Vechicle Name: school volvo Speed: 180 Milege: 12'''
