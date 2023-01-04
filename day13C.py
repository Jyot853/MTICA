def printSunday():
    print("sunday")
def printMonday():
    print("Monday")
def printTuesday():
    print("Tuesday")
def printWednesday():
    print("Wednesday")
def printThursday():
    print("Thursday")
def printFriday():
    print("Friday")
def printSaturday():
    print("Saturday")
def choice():
    print("0.sunday")
    print("1.Monday")
    print("2.Tuesday")
    print("3.Wednesday")
    print("4.Thursday")
    print("5.Friday")
    print("6.Saturday")
weekselection={0:printSunday,1:printMonday,2:printTuesday,3:printWednesday,
               4:printThursday,5:printFriday,6:printSaturday}


while True:
    if selection==7:break
    choice()
    selection=int(input("enter the weeks numbers::"))
    if (selection>=0) and (selection <7):
        weekselection[selection]()   




OUTPUT::
===============================================     
0.sunday
1.Monday
2.Tuesday
3.Wednesday
4.Thursday
5.Friday
6.Saturday
enter the weeks numbers::1
Monday
0.sunday
1.Monday
2.Tuesday
3.Wednesday
4.Thursday
5.Friday
6.Saturday
enter the weeks numbers::2
Tuesday
0.sunday
1.Monday
2.Tuesday
3.Wednesday
4.Thursday
5.Friday
6.Saturday
enter the weeks numbers::
