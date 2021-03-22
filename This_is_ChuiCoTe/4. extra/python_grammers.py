n = 10
a = [0] * n
print(a)

n = 3
m = 4
array = [[0] * m for _ in range(n)]

print(array)

array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

a = [1,2,3,4,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)