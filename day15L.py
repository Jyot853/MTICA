def f():
    x=10
    print('id(x)in f outer:',id(x))
    def g():
        global  x # NONLOCAL #GLOBAL 
        x=15
        print('id(x)in g inner:',id(x))
    g()
    print(x)
f()



'''OUTPUT:
 ==============   
NONLOCAL :  id(x)in f outer: 140723672638536
id(x)in g inner: 140723672638696
15

GLOBAL :
==============
id(x)in f outer: 140723672638536
id(x)in g inner: 140723672638696
10

