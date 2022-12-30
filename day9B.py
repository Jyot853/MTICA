def printseries(n):
    num=1
    for i in range(1,n+1):
        print()
        for j in range(i):
           print(num,end=' ')
           num +=1
    return None
inpNum=int(input('enter a number:'))
printseries(inpNum)



'''output:
enter a number:5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 '''
