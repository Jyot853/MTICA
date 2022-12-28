import time
n=int(input("enter a no:"))
start=time.time()
for i in range(n):
    print("i=",i,"i^2=",i*i)
print("time taken by loop:",(time.time()-start)*100000)



output:-
=======================================
enter a no:10
i= 0 i^2= 0
i= 1 i^2= 1
i= 2 i^2= 4
i= 3 i^2= 9
i= 4 i^2= 16
i= 5 i^2= 25
i= 6 i^2= 36
i= 7 i^2= 49
i= 8 i^2= 64
i= 9 i^2= 81
time taken by loop: 10935.282707214355
