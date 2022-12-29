def div(a,b):
    assert( isinstance(a,int) or isinstance(b,float)),\
            'first argument should be either integer or float'
    assert( isinstance(a,int) or isinstance(b,float)),\
            'second  argument should be either integer or float'        
    assert(b!=0),"division by zero is not defined"
    return a/b
try:
    print(div(55,0))
except AssertionError as ob:
    print(ob)
try:
    print(div(20,3))
except AssertionError as ob:
    print(ob)
try:
    print(div(10,20))
except AssertionError as ob:
    print(ob)
try:
    print(div('hello',20))
except AssertionError as ob:
    print(ob)

