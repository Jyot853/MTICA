def  removeSpecialChar(s):
    ans=[]
    for i in s:
        if (ord(i) in  range(65,91)or ord(i) in range(97,123)
            or ord(i) in range(48,57)):
            ans.append(i)
    return ' '.join(ans)


inp=input()
print(removeSpecialChar(inp))



'''output:
=============
jyothsna.,@gmail.commkldjkOADuitR{- 8
j y o t h s n a g m a i l c o m m k l d j k O A D u i t R 8'''
