lst=[]
while(True):
  n=int(input("enter a values(0 to end):"))
  if n==0:
     break
  else:
    lst.append(n)
lst.sort()

print("min:",lst[0])
print("max:",lst[-1])
print("avg:",round(sum(lst)/len(lst),1))



'''
output::
 ================  
enter a values(0 to end):5
enter a values(0 to end):3
enter a values(0 to end):11
enter a values(0 to end):0
min: 3
max: 11
avg: 6.3'''
