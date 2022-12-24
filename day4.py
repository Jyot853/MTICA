Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello' 'jyothsna' 'good morning'
'hellojyothsnagood morning'
'hello', 'jyothsna', 'good morning'
('hello', 'jyothsna', 'good morning')
"hello", 'jyothsna', 'good morning'
('hello', 'jyothsna', 'good morning')
"hello", "jyothsna", "good morning"
('hello', 'jyothsna', 'good morning')
"hello", "jyothsna", 'good morning'
('hello', 'jyothsna', 'good morning')
'hello'"vennela"'goodmorning'
'hellovennelagoodmorning'
a='hello'"vennela"'goodmorning'
type(a)
<class 'str'>
b=23,47,2.4,'jyothsna',4+7j
type(b)
<class 'tuple'>
b=23,47,2.4,'jyothsna',4+7j,
type(b)
<class 'tuple'>
a=55
b=79
c='jyothsna'
d="vennela"
e=4+7j
f=33.67
g=True
type(a)
<class 'int'>
type(b)
<class 'int'>
type(c)
<class 'str'>
type(d)
<class 'str'>
type(e)
<class 'complex'>
type(f)
<class 'float'>
type(g)
<class 'bool'>
list.append(10)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list.append(10)
TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'int' object
list1.append(10)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list1.append(10)
NameError: name 'list1' is not defined. Did you mean: 'list'?
list1=10
type(list1)
<class 'int'>
list1.append(10)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list1.append(10)
AttributeError: 'int' object has no attribute 'append'
list(list1)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(list1)
TypeError: 'int' object is not iterable
list=(12,23,45,2.3)
type(list)
<class 'tuple'>
list1=[10,20]
type(list1)
<class 'list'>
list1.append(20)
list1.append(40)
list1.append(70)
list1
[10, 20, 20, 40, 70]
list1.clear
<built-in method clear of list object at 0x000001F4A06E9D00>
list1.clear(list1)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list1.clear(list1)
TypeError: list.clear() takes no arguments (1 given)
list1.clear()
list1
[]
list1.count('jyothsna")
            
SyntaxError: unterminated string literal (detected at line 1)
list1.count('jyothsna')
            
0
list1[10, 20, 20, 40, 70]
            
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list1[10, 20, 20, 40, 70]
TypeError: list indices must be integers or slices, not tuple
list1[10,20,30,40]
            
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list1[10,20,30,40]
TypeError: list indices must be integers or slices, not tuple
list1=[10,20,30,40,50]
            
list.append('jyo')
            
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    list.append('jyo')
AttributeError: 'tuple' object has no attribute 'append'
list1=[10,20,30,40,50]
            
type(list1)
            
<class 'list'>
list1.append('jyothsna')
            
list1
            
[10, 20, 30, 40, 50, 'jyothsna']
list1.count()
            
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list1.count()
TypeError: list.count() takes exactly one argument (0 given)
list1.count(2)
            
0
len.list1()
            
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    len.list1()
AttributeError: 'builtin_function_or_method' object has no attribute 'list1'
len(list1())
            
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    len(list1())
TypeError: 'list' object is not callable
list1=[10,20]
            
list1.append(20)
            
list1.append(3)
            
list1.append('jyothsna')
            
list1
            
[10, 20, 20, 3, 'jyothsna']
list1.count()
            
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list1.count()
TypeError: list.count() takes exactly one argument (0 given)
list1.append([29,49])
            
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49]]
list1[:1]
            
[10]
list1[1:]
            
[20, 20, 3, 'jyothsna', [29, 49]]
list1[-3]
            
3
list1[0]
            
10
list1[1:6]
            
[20, 20, 3, 'jyothsna', [29, 49]]
list1[7]
            
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list1[7]
IndexError: list index out of range
list1.remove(2)
            
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list1.remove(2)
ValueError: list.remove(x): x not in list
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49]]
list1.index(10,1)
            
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    list1.index(10,1)
ValueError: 10 is not in list

list1.index(10,10,3)
            
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    list1.index(10,10,3)
ValueError: 10 is not in list
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49]]
list1.count(3)
            
1
list1.count(5)
            
0
list1.count('jyothsna')
            
1
list1.append(3)
            
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49], 3]
list1.count(3)
            
2
list1.extend([29,49])
            
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49], 3, 29, 49]
list1.extend([29,49])
            
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49], 3, 29, 49, 29, 49]
list1.extend([2,4])
            
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49], 3, 29, 49, 29, 49, 2, 4]
list1.index(13,2,9)
            
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list1.index(13,2,9)
ValueError: 13 is not in list
list1(10,1,12)
            
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list1(10,1,12)
TypeError: 'list' object is not callable
list1.index(10,1,12)
            
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    list1.index(10,1,12)
ValueError: 10 is not in list
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49], 3, 29, 49, 29, 49, 2, 4]
list1.index(3,4,11)
            
6
list1.index(2,4,11)
            
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list1.index(2,4,11)
ValueError: 2 is not in list
list1.index(3,4,11)
            
6
list1.index(4,5,11)
            
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    list1.index(4,5,11)
ValueError: 4 is not in list
list1.index(3,4,12)
            
6
list1.pop()
            
4
list1
            
[10, 20, 20, 3, 'jyothsna', [29, 49], 3, 29, 49, 29, 49, 2]
a=list1.pop()
            
vennela
            
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    vennela
NameError: name 'vennela' is not defined
a=list1.pop()
            
a
            
49
a=list1.pop(4)
            
a
            
'jyothsna'
a=list1.pop(7)
            
a
            
49
a=list1.pop(6)
            
a
            
29
a=list1.pop(-1)
            
a
            
29
list1
            
[10, 20, 20, 3, [29, 49], 3]
a=list1.push('jyothsna')
            
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a=list1.push('jyothsna')
AttributeError: 'list' object has no attribute 'push'
list1.append('jyothsna')
            
list1
            
[10, 20, 20, 3, [29, 49], 3, 'jyothsna']
list1.count(3)
            
2
list1.extend([rani,ninna])
            
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    list1.extend([rani,ninna])
NameError: name 'rani' is not defined. Did you mean: 'range'?
list1.extend([40,39])
            
list1
            
[10, 20, 20, 3, [29, 49], 3, 'jyothsna', 40, 39]
list1.index(3,4,7)
            
5
a=list1.pop([29,49])
            
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a=list1.pop([29,49])
TypeError: 'list' object cannot be interpreted as an integer
a=list1.pop(4)
            
a
            
[29, 49]
list1
            
[10, 20, 20, 3, 3, 'jyothsna', 40, 39]
list1.reverse()
            
list1
            
[39, 40, 'jyothsna', 3, 3, 20, 20, 10]
l1=[38,54,66,77,81,2,3]
            
l2=['jyo','venni','ninna','rani']
            
l1
            
[38, 54, 66, 77, 81, 2, 3]
l2
            
['jyo', 'venni', 'ninna', 'rani']
l1.sort(reverse=true)
            
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    l1.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
l1.sort(reverse=True)
            
l1
            
[81, 77, 66, 54, 38, 3, 2]
l2.sort(reverse=True)
            
l2
            
['venni', 'rani', 'ninna', 'jyo']
l2.remove(2)
            
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    l2.remove(2)
ValueError: list.remove(x): x not in list
