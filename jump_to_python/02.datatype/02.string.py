## escapte code ##

#\n 문자열 안에서 줄바꿈

#\t 문자열 사이에 탭간격

#\\ 문자\ 그대로 표현

#\' 작은따옴표 그대로 표현

#\" 큰따옴표 그대로 표현

#\r - 캐리지 리턴(줄바꿈, 커서 가장 앞으로)
 
#\f - 폼 피드(줄바꿈, 커서 다음줄로)

#\a - 벨 소리(출력시 PC 스피커에서 소리)

#\b - 백 스페이스

#\000 - 널문자



## 문자열 포메팅 ##

apple_num = 5

day = "three"

print("I eat %d apples." % apple_num)


print("I eat %s apples." % "five")


print("I ate %d apples. so I was sick for %s days." % (apple_num, day))

# 문자열 포맷 코드 #

# %s 문자열
# %c 문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
# # %% Literal % (문자 % 자체) 

print("I have %s apples" % 3)

print("rate is %s" % 3.224)

print("Error is %d%%." % 98)

# 1. 정렬과 공백 #

# 전체길이 4개인 문자열 공간에서 대입되는 값 오른쪽 정렬
print("%4s" % "hi")
              #this#
# 전체길이 4개인 문자열 공간에서 대입되는 값 왼쪽 정렬
print("%-4sjane." % "hi")
                  #this#

# 2. 소수점 표현 #
# 소수점 4째자리 까지 표기
print("%0.4f" % 3.42134234)
# 자리수 남으면 0으로 채움
print("%0.4f" % 3.4)
# 소수점 4째자리까지 표기 + 전체 길이 10개인 문자열에 오른쪽 정렬
print("%10.4f" % 3.42134234)
print("%-10.4f" % 3.42134234)

# format function # 

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("seven"))

# 여러개 넣기
print("I ate {0} apples. so I was sick for {1} days".format(apple_num, day))
                                                # {n} n이 format()의 인수들 순서에 매칭됨

# 인덱스와 이름 혼용
print ("I ate {0} apples. so I was sick for {day} days".format(10, day=3)) 

# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))

# 공백 채우기, 공백을 지정문자로 대체
print("{0:!<10}".format("hi"))

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

#  {} 문자 표현하기
print("{{ and }}".format())

# f문자열 포매팅 (higeher then v3.6) #

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}입니다.") 

# 정렬
print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬

#공백채우기
print(f'{"hi":=^10}')
print(f'{"hi":!^10}')

#소수점 표현
y=3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')

# {}문자 표현
print(f'{{ and }}')

# 문자열 관련 함수 #

# count()
a = "hobby"
print(a.count('b'))


# find()
a = "Python is the best choice"
print(a.find('b')) #0에서부터
print(a.find('k')) #없는 문자 -1반환

# index()
a = "Life is too short"
print(a.index('t'))
# print(a.index('k')) #없는 문자 찾으면 오류

# join()
print(",".join('abcd'))
print(",".join(['a','b','c','d']))


# lower()
a = "HI"
print(a.lower())

# upper()
a =  "hi"
print(a.upper())

# lstrip()
a = " hi"
print(a.lstrip())

# rstrip()
a = "hi "
print(a.rstrip())

# strip()
a = " hi "
print(a.strip())

# split()
a = "Life is too short"
print(a.split()) # 공백기준으로 나눔
b = "a:b:c:d"
print(b.split(':')) # 지정된 문자 기준으로 나눔