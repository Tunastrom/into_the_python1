class Cacluator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        self.value += val

class UpgradeCalculator(Cacluator):
    
    def minus(self, val):
        self.value += -1*(val)
         
   
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)