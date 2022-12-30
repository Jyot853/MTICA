def printseries(n):
    for i in range(1,n+1):
         num=1
         print()
         for j in range(i):
           print(num,end=' ')
           num+=1
          
    return None
inpNum=int(input('enter a number:'))
printseries(inpNum)


'''output:

    
enter a number:6
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
'''
