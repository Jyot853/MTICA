spins=[('Red','18'),('Black','13'),('Red','7'),('Black','5'),
       ('Red','18'),('Black','13'),('Red','25'),('Black','9'),
       ('Red','26'),('Black','15'),('Red','20'),('Black','3'),
       ('Black','13'),('Black','15'),('Red','20'),('Black','3')]
def countReds(aList):
    count=0
    for color,Number in aList:
        if color=='break':
            yield count
            count=0
        else:
            count +=1
    yield count
gaps=[gap for gap in countReds(spins)]
print(gaps)


OUTPUT:
    [16]
