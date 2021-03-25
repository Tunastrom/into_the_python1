# 변수 선언
numbers = [1,2,3,4,5,6]
e_num = enumerate(numbers)
print(id(e_num))
# reversed_numbers를 출력
print("enumerated_numbers: ",e_num)
for i in range(len(numbers)):
    print(next(e_num))

# e_num = enumerate(numbers)
print(id(e_num))
print("enumerated_numbers: ",e_num)
for i in range(len(numbers)): print(next(e_num))