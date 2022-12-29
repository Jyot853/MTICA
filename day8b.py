def Factorial(num):
    assert(num>=0),"Factorial number is not defined by negative number"
    assert(isinstance(num,int)),"Factroical of negative numbers is nioyt defined"
    if num==0:
       return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-46))
except Exception as obj:
    print(obj)
try:
    print(Factorial(8.8))
except Exception as object:
    print(object)
try:
    print(Factorial(88))
except Exception as object:
    print(object)
try:
    print(Factorial('jyothsnarani'))
except Exception as object:
    print(object)
           
