# 기존 dictionary update
print('# 기존 dictionary update')
a = dict(a='abc', b='bcd')
b = dict(c='cde', e='efg')

a.update(b)
print(a)

c = { **a, **b }
print(c)

# New dictionary update 
print('# New dictionary update')
x = {'key1':'value1 from x', 'key2':'value2 from x'}
y = {'key2':'value2 from x', 'key3':'value3 from x'}

print(x | y)
print(y | x)
x|=y
print(x)


