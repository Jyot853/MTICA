def printseriesDecreasing(ch,n):
    assert isinstance(ch,str),'first argument is string'
    assert isinstance(n,int),'second argument should be integer'
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpch=input("enter a character:")
inpNum=int(input("enter a number:"))
print('-'*40)
try:
    printseriesDecreasing(inpch,inpNum)
except AssertionError as obj:
    print(obj)
    

