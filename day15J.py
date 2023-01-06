def f():
    x=10
    def  g():
      global  x      # nonlocal  # global
      x=1
    g()
    print(x)
f()



'''output:
============
    nonlocal    1
    global       10  '''
