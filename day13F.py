def sum_num(x):
    res=0
    for i in range(x+1):
        res=res+i
        yield("i=",i,"res=",res)
    return res
ob=sum_num(10)
for i in range(11):
    print(next(ob))
    


output:
=============================
('i=', 0, 'res=', 0)
('i=', 1, 'res=', 1)
('i=', 2, 'res=', 3)
('i=', 3, 'res=', 6)
('i=', 4, 'res=', 10)
('i=', 5, 'res=', 15)
('i=', 6, 'res=', 21)
('i=', 7, 'res=', 28)
('i=', 8, 'res=', 36)
('i=', 9, 'res=', 45)
('i=', 10, 'res=', 55)
    
