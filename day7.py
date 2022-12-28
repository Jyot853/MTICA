string='''practice problems for list com pre hension in python.'''
wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n")for i in wordsLst ]
print(wordsLst)
ans={i:len(i) for i in wordsLst}
print(ans)



'''output:
    ['practice', 'problems', 'for', 'list', 'com', 'pre', 'hension', 'in', 'python.']
['practice', 'problems', 'for', 'list', 'com', 'pre', 'hension', 'in', 'python.']
{'practice': 8, 'problems': 8, 'for': 3, 'list': 4, 'com': 3, 'pre': 3, 'hension': 7, 'in': 2, 'python.': 7}
'''
