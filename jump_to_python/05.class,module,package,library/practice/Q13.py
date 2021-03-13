import random

lucky_numbers = set()  

while len(lucky_numbers) <= 6: 
    lucky_numbers.add(random.randint(1,45)) 

print(lucky_numbers)