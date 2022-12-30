def printseries(ch,i):
    sp='.'
    for i in range(0,i):
        print(sp*(i-i-1)  +ch*(2*i+1)+sp*(i-i-1))
    return None
inpch=input()
inpNum=int(input())
printseries(inpch,inpNum)


output:
    
*
4
*
***
*****
*******
