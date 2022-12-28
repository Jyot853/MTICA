print("int: {0:d}; hex: {0:x}; oct: {0:o};bin: {0:b}".format(42,55))
print("int: {1:d}; hex: {1:x}; oct: {1:o};bin: {1:b}".format(42,55))
print('{:,}'.format(1234567890))
points=19.0; total=22
print('correct answer: {:.2%}'.format(points/total))
print('correct answer: {:.2}'.format(points/total))

'''output:
================   
nt: 42; hex: 2a; oct: 52;bin: 101010
int: 55; hex: 37; oct: 67;bin: 110111
1,234,567,890
correct answer: 86.36%'''
