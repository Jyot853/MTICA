def squares(x=0):
    while x<30:
        x=x+1
        yield x*x
yieldedList=list(squares())
print(yieldedList)



'''output:
================================ 

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''
