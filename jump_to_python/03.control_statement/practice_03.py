# 1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# first_answer = input("answer: ")

# print("answer: {0}".format(answer))

# 2 
int_num = 0
total_Multiples_3 = 0
while int_num <= 1000:
    if int_num % 3 == 0:
        total_Multiples_3 += int_num
    int_num += 1
print("2. {0}".format(total_Multiples_3))    
        
#3
row = 1
while row <= 5:
    print("*" * row)
    row = row + 1


# 4    

for i in range(1,101):
    print(i)

# 5

# def average (*args):
    
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]  

total_scores = 0
for score in scores:
    total_scores += score
avarage = total_scores / len(scores)

print(avarage)

# def avarage(*args):
#     for i in args:

#6

numbers = [1,2,3,4,5]
result = [ n * 2 for n in numbers if n % 2 == 1]
print(result)


