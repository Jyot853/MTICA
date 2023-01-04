def printBlue():
    print('you chose Blue!\n')
    return
def printRed():
    print('you chose Red!\n')
def printOrange():
    print('you chose Orange!\n')
def printYellow():
    print('you chose Yellow!\n')    

def choice():
  
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
colorselect={0:printBlue,1:printRed,2:printOrange,3:printYellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("secect color one:"))
    if (selection>=0)and(selection<4):
        colorselect[selection]()






outpur:
    




        you chose Yellow!

0:Blue
1:Red
2:Orange
3:Yellow
4:Quit
secect color one:1
you chose Red!

0:Blue
1:Red
2:Orange
3:Yellow
4:Quit
secect color one:6
0:Blue
1:Red
2:Orange
3:Yellow
4:Quit
secect color one:8
0:Blue
1:Red
2:Orange
3:Yellow
4:Quit
secect color one:3
you chose Yellow!

0:Blue
1:Red
2:Orange
3:Yellow
4:Quit
secect color one:2
you chose Orange!

0:Blue
1:Red
2:Orange
3:Yellow
4:Quit
secect color one:
