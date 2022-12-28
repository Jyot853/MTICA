>>>dict1={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":7,"montocycle":110}
dict1
{'sedan': 1500, 'suv': 2000, 'pickup': 2500, 'minivan': 1600, 'van': 2400, 'semi': 13600, 'bicycle': 7, 'montocycle': 110}

>>>dict1.keys()
dict_keys(['sedan', 'suv', 'pickup', 'minivan', 'van', 'semi', 'bicycle', 'montocycle'])
>>>dict1.values()
dict_values([1500, 2000, 2500, 1600, 2400, 13600, 7, 110])
>>>dict1.items()
dict_items([('sedan', 1500), ('suv', 2000), ('pickup', 2500), ('minivan', 1600), ('van', 2400), ('semi', 13600), ('bicycle', 7), ('montocycle', 110)])



>>>for i in dict1:
    print(i)
   
sedan
suv
pickup
minivan
van
semi
bicycle
montocycle



>>>for i in dict1:
    if dict1[i]<5000:
        print(i)       
sedan
suv
pickup
minivan
van
bicycle
montocycle




>>>for i in dict1:
    if dict1[i]<500:
        print(i.upper())

        
BICYCLE
MONTOCYCLE
