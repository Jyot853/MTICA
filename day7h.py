dict1={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":7,"montocycle":110}
for i in dict1:
    if dict1[i]<500:
        print(i.upper())