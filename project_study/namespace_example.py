# 0. namespace = 프로그래밍 언어에서 특정한 object를 name에 따라 구분할 수 있는 범위

# 1. A namespace is a mapping from name to object 

# 2. Most namespace are currently implemented as Python dictionaries, but that's normally not noticeable in any way.

# 3. Examples
#   - the set of built-in names
#   - the global names in a moudule
#   - the local names in a function invocation. 
#   - In a sense the set of attributes of an object also form a namespace

# 4. important thing to know
#   : There is no reration between names in different namespaces

# 5. natures
#   - 네임스페이스는 딕셔너리 형태로 구현됨.
#   - 모든 이름 자체는 문자열이고, 각각은 자신이 속한 네임스페이스의 범위에서 실제 객체를 가리킴.
#   - 이름과 실제 객체 사이의 매핑은 가변적(Mutable), 런타임 동안 새 이름 추가 가능.
#   - built-in 네임스페이스는 함부로 추가하거나 삭제 불가

# 6. Variable Scope
#   : 접두어(prefix) 없이 어떤 네임스페이스에 직접 접근이 가능한 코드의 일정 부분.
#     python just have global variable scope and local variable scope.
#    - 지역 이름들을 포함하는 현재 함수의 스코프 = 지역 네임스페이스
#    - 전역 이름들을 포함하는 현재 모듈의 스코프 = 전역 네임스페이스
#    - 빌트인 이름들을 포함하는 최외곽의 스코프 = 빌트인 네임스페이스
  
# 포함관계
# Built-in Namespace> Module: Global Namespace > Function: Local Namespace 
  
# def outer_func():
#     a = 20
#     def inner_func():
#         a = 30
#         print( "a = %d" % a )

#     inner_func()
#     print("a = %d" % a)

# a = 10
# outer_func()
# print("a = %d" % a)


# def outer_func():
#     a = 20
#     def inner_func():
#         a = 30
#         print( locals() )

#     inner_func()
#     print( locals() )

# a = 10
# outer_func()
# print( locals() )


#  '__name__': '__main__'

def outer_func():
    a = 20
    def inner_func():
        a = 30

    inner_func()

a = 10
outer_func()
print("Namespace:", globals()["__name__"])


### python의 메인모듈 형식 ###

# def main():
#     #...
#
# if __name__ == '__main__':
#     main()


# if __name__ == '__main__'
# -> 현재 모듈의 네임스페이스가 __main__ 일때 if문 이하 실행
#    = 현재 모듈이 커맨드라인 상에서 직접실행되는 경우에만 if문 이하 실행     




