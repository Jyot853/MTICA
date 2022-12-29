num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
try:
    re=num1/num2
except ZeroDivisionError:
    print("Division  by zero not allowed")
else:
    print(num1, '/' ,num2, '=',res)
print('thanks')





'''output:
========================
enter a number:2
enter a number:0
Division  by zero not allowed
thanks'''
