def demo_yield():
    print("code segment1 executed")
    x=7
    yield x*x
    print("code segment2 executed")
    yield 2
    print("code segment3 executed")
    yield 3
    print("code segment4 executed")


output:
==============================
type(demo_yield)
<class 'function'>
x=demo_yield()
type(x)
<class 'generator'>
next(x)
code segment1 executed
49
next(x)
code segment2 executed
2
next(x)
code segment3 executed
3
next(x)
code segment4 executed
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    next(x)
StopIteration
    
