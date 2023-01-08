### removeSpecialChar


def  removeSpecialChar(s):
    ans=[]
    for i in s:
        if i in '0123456789ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrstuvwxyz':
             ans.append(i)
    return ' '.join(ans)


inp=input()
print(removeSpecialChar(inp))



'''output:
=========
jyisdytsgxhjkh\@2gmakjxioUs121
j y i s d y t s g x h j k h 2 g m a k j x i o s 1 2 1'''
