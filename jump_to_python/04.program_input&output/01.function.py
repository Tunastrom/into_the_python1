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

def say_myself(name, old, man=True):
    print("")