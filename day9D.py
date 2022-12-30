def printseries(n):
    num=1
    for i in range(1,n+1):
        print()
        for j in range(i):
           print(n,end=' ')
          
    return None
inpNum=int(input('enter a number:'))
printseries(inpNum)



'''output:
    
enter a number:5
5 
5 5 
5 5 5 
5 5 5 5 
5 5 5 5 5 '''
