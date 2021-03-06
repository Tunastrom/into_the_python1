class FourCal:
    # Method
    def __init__(self, first, second): # Constructor: 객체가 생성될 때 자동 호출되는 메서드 
        self.first = first
        self.second = second

    def setdata(self, first, second):
                # 매개변수 self #
                # FourCal 클래스의 인스턴스 a가 setdata 메소드를 호출하면
                # 호출한 객체 a가 self로 전달된다.
        self.first = first
        self.second = second
        # a.first = 4 문장 수행되면 a객체에 객체변수 first 생성 및 값 4 저장
                                          # 객체에 생성되는 객체만의 변수                             
    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
        
    def div(self):
        result = self.first / self.second
        return result
          



# a = FourCal(4, 2)
# b = FourCal(8, 5)

# # a.setdata(4,2)
# # b.setdata(3,7)
# # print(a.first)
# # print(a.second)
# # print(id(a.first))
# # print(id(b.first))
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# print(b.add())
# print(b.sub())
# print(b.mul())
# print(b.div())





