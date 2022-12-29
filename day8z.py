def checkEvenOdd(num1):
    if num1%2==0:
        return "even"
    else:
        return "odd"
for i in range(9):
    num=int(input("enter a values::"))
    print(num,"is",checkEvenOdd(num))

