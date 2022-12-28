string='''practice problem for list comprehesion in python'''

ans=[i  for i in string  if i not in 'AEIOUaeiou' ]
print(*ans)

output:
========================
    p r c t c   p r b l m   f r   l s t   c m p r h s n   n   p y t h n

