string='''practice problems for list com pre hension in python.'''
wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n")for i in wordsLst ]
print(wordsLst)
ans={i:i[::-1] for i in wordsLst}
print(ans)


output:
    
['practice', 'problems', 'for', 'list', 'com', 'pre', 'hension', 'in', 'python.']
['practice', 'problems', 'for', 'list', 'com', 'pre', 'hension', 'in', 'python.']
{'practice': 'ecitcarp', 'problems': 'smelborp', 'for': 'rof', 'list': 'tsil', 'com': 'moc', 'pre': 'erp', 'hension': 'noisneh', 'in': 'ni', 'python.': '.nohtyp'}
