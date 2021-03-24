numbers = [1,2,6,8,4,3,2,1,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number not in counter:
         counter[number] = 1 
    elif number in counter:
        counter[number] += 1

print(counter)