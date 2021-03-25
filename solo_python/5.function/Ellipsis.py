import numpy as np

def do_something():
    raise NotImplementedError()

a= [1,2,3,4,5,6]
print(a[:])

b = [[1,2,3], [4,5,6]]
print(b[:][:])
print(b[1][:])

c = np.array(b)
print(c)

print(c[:,:])

print(c[...])

d = np.array([[[i + 2 * j + 8 * k for i in range(3)] for j in range(3)] for k in range(3)])
print(d)

print(d[...,0])

do_something()
