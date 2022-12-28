>>>print('{0},{1},{2}'.format('jyothsna','vennela','nanna','amma'))
jyothsna,vennela,nanna
>>>print('{0},{1},{2},{3}'.format('jyothsna','vennela','nanna','amma'))
jyothsna,vennela,nanna,amma
>>>print('{0},{1}{3}{2}{2},{3}'.format('jyothsna','vennela','nanna','amma'))
jyothsna,vennelaammanannananna,amma
>>>print('{0},{1},{3},{2},{2},{3}'.format('jyothsna','vennela','nanna','amma'))
jyothsna,vennela,amma,nanna,nanna,amma


==========================================================================================

>>>print('{},{},{}'.format('apple','banana','mango'))
apple,banana,mango
>>>print('jyothsna  purchesed by{},vennela eating {},manasa likes{}'.format('apple','banana','mango'))
jyothsna  purchesed byapple,vennela eating banana,manasa likesmango


==========================================================================================

>>>print('jyothsna  purchesed by{0}and{1},vennela eating {2}and{0},manasa likes{1}and{0}'.format('apple','banana','mango'))
jyothsna  purchesed byappleandbanana,vennela eating mangoandapple,manasa likesbananaandapple

==========================================================================================

>>>print('{2},{1},{0}'.format(*'abcd'))
c,b,a
>>>x,*y,z='computer'
>>>x
'c'
>>>y
['o', 'm', 'p', 'u', 't', 'e']
>>>z
'r'
>>>x,y
('c', ['o', 'm', 'p', 'u', 't', 'e'])
>>>x,z
('c', 'r')
>>>y,z
(['o', 'm', 'p', 'u', 't', 'e'], 'r')
==============================================================================================================================

>>>print('coordinatesw:{latitude},{longitude}'.format(latitude='37.24N',longitude='-115.81W'))
coordinatesw:37.24N,-115.81W

============================================================================================================

>>>print('welcome:{name},your college is:{college}'.format(name='jyothsna',college='MTICA'))
welcome:jyothsna,your college is:MTICA

============================================================================================================
>>>student={43:'revi',42:'sree'}
>>>type(student)
<class 'dict'>
>>>student.keys()
dict_keys([43, 42])
>>>student.values()
dict_values(['revi', 'sree'])

