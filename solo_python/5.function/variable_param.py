import sys


def print_n_times(*values, n=2):
    # n번 반복합니다.
    for i in range(n):
        # variables는 리스트처럼 활용합니다.
        for value in values:
            ## print()의 기본형태
            print(value, ..., sep='', end='\n', file=sys.stdout, flush=False)
        # 단순한 줄바꿈
        print()

# 함수를 호출합니다.
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", 3)

def print_n_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)

# 함수를 호출합니다.
print_n_times("안녕하세요")