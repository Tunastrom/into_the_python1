
# normal list

size = 10
arr1 = [0] * size
for i in range(len(arr1)):
    arr1[i] = i * 2

print(arr1)


# list comprehension
size = 10
arr2 = [i * 2 for i in range(size)]
print(arr2)

print(size[0])