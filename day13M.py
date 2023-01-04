def add(n1,n2):
    temp=n1+n2
    #global variables:a,b,c,add
    #local variables:n1,n2 ,temp
    global a,b
    a+=10
    print("output of globals:",globals())
    print("output of locals:",locals())
    return temp
a=int(input())
b=int(input())
c=add(a,b)
print(a,'+',b,'=',c)


'''OUTPUT:
==============================
11
22
output of globals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/pythonpractice(24)/day13/day13M.py', 'add': <function add at 0x0000021411918AE0>, 'a': 21, 'b': 22}
output of locals: {'n1': 11, 'n2': 22, 'temp': 33}
21 + 22 = 33'''

