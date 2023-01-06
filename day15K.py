def myfunc1():
    x="josh"
    def myfunc2():
       global x#  global #nonlocal
       x="hello"
    myfunc2()
    return x
print(myfunc1())



'''OUTPUT:

NONLOCAL    hello
GLOBAL          josh      '''
 
