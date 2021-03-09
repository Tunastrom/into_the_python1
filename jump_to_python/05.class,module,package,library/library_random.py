import random
#  0.0 ~ 1.0사이의 실수중에서 난수값 반환 
print(random.random())
# 1에서 10사이의 정수 중 난수값
print(random.randint(1, 10))
# 1에서 55사이의 정수 중 난수값
print(random.randint(1, 55))

## 리스트 요소중 무작위 하나 선택해 pop
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)


def random_pop_c(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

data = [1,2,3,4,5]
# 리스트 순서 무작위로 섞어서 반환
random.shuffle(data)
print(data)


