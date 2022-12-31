fo=open(r"E:\pythonpractice(24)\day10\jyoti1.txt","w+")
for i in range(3):
    inp=input()
    fo.write(inp+'\n')
fo.close()
print("writem to file")
