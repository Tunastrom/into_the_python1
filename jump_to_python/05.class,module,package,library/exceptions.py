### try except ###

## cases ##
## 1. try, except only
# try:
#     ... 
# except:
#     ...
    
## 2. 발생오류만 포함한 except    
# try:
#     ... 
# except 발생오류:
#     ...    

## 발생 오류와 오류 메시지 변수까지 포함한 except
# try:
#     ... 
# except 발생오류 as 오류메시지 변수:
#     ...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

### try finally ###


# from 
# f = open('foo.txt', 'w')
# try:

# finally:
#     f.close()     
# -> 예외 발생 여부와 관계없이 finally 절에서 열린 파일닫기 

### 여러개의 오류처리 ###
# try:
#    ...
# except 발생 오류1:
#    ...
# except 발생 오류2:
#    ...

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError )as e:
    print(e)

## try 문에 else 절 사용
# try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...
# else: #오류 없을 경우에만 수행됨.
#     ... 

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
# 오류가 없을 시에만 아래 else절을 타고 들어간다.
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

### 오류 회피 ###
try:
    f = open('없는 파일', 'r')
except FileNotFoundError:
    pass

## 인위적 오류 발생 ##
class Bird:
    def fly(self):
        raise NotImplementedError
              # 파이썬 내장 오류, 

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


### 예외 만들기 ###

class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'
    
   
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다.")

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)





