# python keywords

Keywords = set(['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise','return', 'try', 'while', 'with', 'yield'])

# python Reserved Words

Reversed_Words = set([ 'and', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield' ])

### keyword > Reserved Words ###

# print(Keywords & Reversed_Words)
# print(Keywords | Reversed_Words)
# print(Keywords - Reversed_Words)
# print(Reversed_Words - Keywords) 


## 여러개의 argument 받는 함수 ##
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5))

def add_many1(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_many1(1,2,3))

print(add_many1(1,2,3,4,5,6,7,8,9,10))
print(add_many(1,2,3,4,5,6,7,8,9,10))


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


prompt = '''
1, 2, 3, 4, 5에 대한 작업을 입력하세요

1. add

2. mul
''' 

# print(add_mul(input(prompt), 1,2,3,4,5))


## keyword parameter 'kwargs'

def print_kwargs(**kwargs):
    print(kwargs)

print(print_kwargs(a=1))

print(print_kwargs(name='foo', age=3))


def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

def say_myself(name, old, man=True): #초기화할 변수는 항상 맨 뒤에
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:   
        print("여자입니다.")


say_myself("유철원", 29)
say_myself("강혜원", 23, False)

a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

vartest(3)
print(a)



def vartest_global():
    global a
    a = a + 1

vartest_global()
print(a)  

add = lambda a, b: a+b
     # lambda 매개변수1,매개변수2...: 매개변수 이용한 표현식 
     # return 없이도 결과값 돌려줌
result = add(3,4)



def add(a,b):
    return a+b
result = add(3,4)
print(result)




