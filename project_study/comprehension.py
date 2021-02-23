## 2021.02.23

# Python Comprehension

# List Comprehension : [출력표현식 for 요소 in 입력Sequence [if조건식]]

oldlist_L = [1,2,'a', False, 3]

newlist_L = [i*i for i in oldlist_L if type(i)==int]

print(newlist_L)


# Set Comprehension : {출력표현식 for 요소 in 입력Sequence [if조건식]}

# Return set 

# Sequence에서 for문으로 요소 1개씩 꺼내 if 조건식에 맞는 값만 출력표현식을 거친후 set으로 담아 리턴

oldlist_S = [1, 1, 2, 3, 3, 4]

newlist_S = {i*i for i in oldlist_S}

print(newlist_S)

# 결과값이 담기는 Set은 중복을 허용하지 않아, 결과값은 중복이 제거된다. 


# Dictionary Comprehension : {Key:Value for 요소 in 입력Sequence [if 조건식]}

# return Dictionary

id_name = {1: '최예나', 2: '이채연', 3:'김민주', 4:'강혜원', 5:'장원영', 6:'조유리'}

name_id = {val:key for key,val in id_name.items() if val[0] == "김" }

print(name_id)

# if 조건식에 필터링 함수 사용

def isodd(val):
    return val % 2 == 1

mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict)