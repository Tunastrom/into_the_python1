##2021.02.23

# iteratrable

mylist1 = [1,2,3]
for i in mylist1:
    print(i)

# mylist is iterable

# generators
# : iterator의 일종, 모든 값을 메모리에 담지 않고 그때그때 값을 생성(generation) 해서 반환하는 차이
#   -> 한 번에 한개의 값만 순환(iterate)
#   -> 리소스에 대한 제어가 필요할때 매우 유용

mygenerator1 = (x * x for x in range(3)) 
                   # Python Comprehension
for i in mygenerator1:
    print(i)

# yield #
# return과 비슷한 기능, 차이: generator 반환

def createGenerator():
    mylist2 = range(3)
    for i in mylist2:
        yield i * i

mygenerator2 = createGenerator() # 호출해도 함수내의 코드들이 실행되지 않음.
print(mygenerator2)
for i in mygenerator2: #여기서 실제로 실행됨.   
    print(i)

# 1번째 실행은 함수내에서 yield 만날때까지 실행후 값 반환 
# 그 이후는 yield 뒤의 코드 실행 후 다시 루프 돔 
# 더이상 yield와 만나지 못할때 끝난 것으로 간주   

class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()
corner_street_atm = hsbc.create_atm()
print(corner_street_atm.__next__())
print(corner_street_atm.__next__())
print([corner_street_atm.__next__() for cash in range(5)])
hsbc.crisis = True
# print(corner_street_atm.__next__())
wall_street_atm = hsbc.create_atm()
# print(wall_street_atm.__next__())
hsbc.crisis = False
print(corner_street_atm.__next__())
brand_new_atm = hsbc.create_atm()
for cash in brand_new_atm:
    print(cash)


