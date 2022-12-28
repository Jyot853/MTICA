def add_five(x):
    temp=x+5
    return temp

nums=[11,22,33,44,55,666,777]
result=list(map(add_five,nums))
print(nums)
print(result)
print('-'*40)

output:
---------------------
[11, 22, 33, 44, 55, 666, 777]
[16, 27, 38, 49, 60, 671, 782]
----------------------------------------
