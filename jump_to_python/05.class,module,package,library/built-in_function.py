print(f"{'abs()':-^11}")
print(abs(3))
print(abs(-3))
print(abs(-1.2))

print(f"{'all()':-^11}")
print('입력인수: iterable\niterable의 요소가 모두 참이면 True, 아니면 false')
print(all([1,2,3]))
print(all([1,2,3,0]))
print(all([])) # 입력인수가 빈값일 때 True

if []:
    print("true!")
print('false!')

print(f"{'any()':-^11}")
print('입력인수: iterable\n 인수의 요소중 하나라도 참이면 True, 모두 거짓일때 False')
print(any([1,2,3,0]))
print(any([0, ""]))
print(any([])) # 입력인수가 빈 값일 때 False


print(f"{'chr()':-^11}")
print('ASCII 코드 값 입력 -> 해당하는 문자 출력')
print('*ASCII 코드는 0~127사이 숫자를 각각 문자 또는 기호에 대응시킨 것')
print(chr(97))
print(chr(48))

print(f"{'dir()':-^11}")
print('객체가 가진 변수나 함수 표시')
print(dir([1,2,3]))
print(dir({'1':'a'}))

print(f"{'divmod()':-^11}")
print('2개의 숫자(a,b)를 입력으로 받아, (a//b, a % b)반환')
print(divmod(7,3))

print(f"{'enumerate()':-^13}")
print('= 열거하다. 입력인수: iterable\n 인덱스 값 포함하는 enumerate객체 반환')
print('입력받은 문자열로 파이썬 함수나 클래스 동적실행시 사용')
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i,name)

print(f"{'eval()':-^13}")
print('=expression. 입력인수: 실행가능한 문자열\n 문자열을 실행한 결과값 반환')
print(eval('1+2'))
print(eval('"hi"+"a"'))
print(eval('divmod(4,3)'))

print(f"{'filter()':-^13}")
print('인수1: 함수이름,\n인수2: 인수1에 적힌 함수에 들어갈 iterable')
print('인수2의 iterable이 인수1의 함수에 입력되었을 때 반환값이 참인 것만 걸러내서 반환')

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))


def positive1(x):
    return x > 0 # True, False반환하므로 조건문의 역할

print(list(filter(positive1, [1,-3,2,0,-5,6])))

print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6])))

print(f"{'hex()':-^13}")
print('입력인수: 정수 -> 16진수(hexadecimal)로 반환')
print(hex(234))
print(hex(3))

print(f"{'id()':-^13}")
print('입력인수: 객체,\n객체의 고유 주소값(reference)반환')
a=3
print(id(3))
print(id(a))
b=a
print(id(b))

print(f"{'hex()':-^13}")
print('input[prompt]')
print('* []기호 = 안의 내용 생략가능(관례표기)')
print('사용자입력을 받는 함수\n매개변수로 문자열 -> 프롬프트가 된다.')
a=input()
print(a)
b=input('enter: ')
print(b)

print(f"{'int()':-^13}")
print(int('3'))
print(int(3.4))
print('int(x, radix)\nradix진수로 표현된 문자열 x 10진수로 반환' )
print(int('11',2))
print(int('1A',16))

print(f"{'isinstance()':-^13}")
print('인수1: 인스턴스, 인수2: 클래스 이름\n 입력받은 인스턴스가 입력받은 클래스의 인스턴스인지 판단 참:True/거짓:False')
class Person: pass
a = Person()
print(isinstance(a,Person))
b = 3
print(isinstance(b,Person)) 




