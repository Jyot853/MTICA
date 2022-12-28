method:1
==========================
string=input()
ans=[]
for i in string:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)



method:2
==========================
ans=[i  for i in string  if i in 'AEIOUaeiou' ]
print(*ans)




output:
==========================
my name is jyothsnarani
a e i o a a i
0
=====================================
my name is purushothama reddy
a e i u u o a a e
0
 ===================
my father name is mondam purushothama reddy
a e a e i o a u u o a a e
0
==================================
my mother name mondam bhagya lakshmi
o e a e o a a a a i
0
================================
my sister is vennela rani
i e i e e a a i
0
