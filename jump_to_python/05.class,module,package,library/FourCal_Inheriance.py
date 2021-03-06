from FourCal import FourCal

class MoreFourCal(FourCal):
                 #FourCal 클래스를 상속함을 표시
    
    def pow(self):
        result = self.first ** self.second
        return result
    
class SafeFourCal(FourCal):
     def div(self):
         if self.second == 0:
             return 0
         else:
             return self.first / self.second     
    
a = MoreFourCal(4,0)
print(a.add(), a.mul(), a.sub(), a.div())
print(a.pow())
print(a.div())
