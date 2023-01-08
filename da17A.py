import sys
print("comin through stdout")
save_stdout=sys.stdout
fh=open(r"C:\jyothsna24\day17.txt","w")
sys.stdout=fh
print("this line goes to test.txt")
print(input())
sys.stfout=save_stdout
fh.close()
