import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i ==0:
        print("Function name:{0}".format(sys.argv[0]))
    else:
        print("{0}.argument:{1}".format(i,sys.argv[i]))
        

'''output:


Microsoft Windows [Version 10.0.19044.2364]
(c) Microsoft Corporation. All rights reserved.

C:\jyothsna24\day17>day17.py jyothsna  mca mtica
['C:\\jyothsna24\\day17\\day17.py', 'jyothsna', 'mca', 'mtica']
Function name:C:\jyothsna24\day17\day17.py
1.argument:jyothsna
2.argument:mca
3.argument:mtica

C:\jyothsna24\day17>'''

