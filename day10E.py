def printdetails(name,marks,course):
    print("name:",name)
    print("marks:",marks)
    print("course:",course)
    return None
####printdetails()
##TypeError: printdetails() missing 3 required positional arguments: 'name', 'marks', and 'course'
####printdetails('jyothsna')
##TypeError: printdetails() missing 2 required positional arguments: 'marks' and 'course
####printdetails('jyothsnarani',100,'mca')
##name: jyothsnarani marks: 100 course: mca
####printdetails(100,'jyothsna','mca')
##name: jyothsnarani marks: 100 course: mca
printdetails(name='jyothsna',marks=100,course='MCA')
