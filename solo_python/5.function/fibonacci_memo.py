# 메모변수 생성
dictionary = {
    1: 1,
    2: 1
}

# 함수 선언
def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output


print('fibonacci(10): ', fibonacci(10))
print('fibonacci(20): ', fibonacci(20))
print('fibonacci(30): ', fibonacci(30))
print('fibonacci(40): ', fibonacci(40))
print('fibonacci(50): ', fibonacci(50))
