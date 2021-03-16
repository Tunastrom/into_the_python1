def is_odd(number):
    answer = ""
    # 짝수
    if number % 2 == 0:
        answer = "짝수"
    elif number % 2 == 1:
        answer = "홀수"
    return answer

print(is_odd(1))
print(is_odd(2))

is_odd = lambda x: True if x % 2 == 1 else False
print(is_odd(3))
