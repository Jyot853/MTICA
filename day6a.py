lstEven=[]
lstOdd=[]
while(True):
  n=int(input("enter a values(-1 to end):"))
  if n==-1:
      break
  elif n%2==0:
     lstEven.append(n)
  elif n%2==1:
     lstOdd.append(n)
     
print("Even:",*lstEven)
print("min:",min(lstEven))
print("max:",max(lstEven))
print("Avg:",round(sum(lstEven)/len(lstEven),1))

print("Odd:",*lstOdd)
print("min:",min(lstOdd))
print("max:",max(lstOdd))
print("Avg:",round(sum(lstOdd)/len(lstOdd),1))


