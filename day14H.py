class A:
    def   first_method (self):
        print("method of  class A...")
            
class B :
    def   second_method (self):
        print("method of  class B...")
             
class C (A,B):#B,A
    def   third_method (self):
        print("method of   class C...")
            
            
if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.second_method()
    ob.third_method()
       
'''OUTPUT:
=================
method of  class A...
method of  class B...
method of   class C...'''

