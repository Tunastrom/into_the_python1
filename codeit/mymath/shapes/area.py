__all__ = ['circle']

from mymath.stats.average import data_mean

from . import PI

# 원의 면적을 구해주는 함수
def circle(radius):
    return PI * radius * radius


# 정사각형의 면적을 구해주는 함수
def square(length):
    return length * length

