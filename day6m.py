method:1
========= 
n=input()
ans=[]
for i in n:
    if i in '0123456789':
        ans.append(i)
print(*ans)


method :2
==================
n=input()
ans=[i for i in n if i in '0123456789']
print(*ans)



output:
=================
today is mondey 22/12/2022 day06
2 2 1 2 2 0 2 2 0 6'''
