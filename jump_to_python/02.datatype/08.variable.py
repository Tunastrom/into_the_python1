a = [1,2,3]
# id() 변수가 가리키는 객체의 주소 값 반환 built-in function
print(id(a))

b = a 

print(id(a))
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

b=  a[:]
a[1] = 5
print(a)
print(b)
print(id(a))
print(id(b))

from copy import copy

b = copy(a)

print(b is a)

## 변수 만드는 방법들

a ,b = ('python', 'life')
(a, b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python' 

print(a, b)
a,b = 3,5
print(a,b)
a, b = b, a
print(a,b)