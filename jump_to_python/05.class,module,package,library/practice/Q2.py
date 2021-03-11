class MaxLimitCaculator:
    
    def __init__ (self):
        self.value = 0

    def add(self, val):
        self.value += val 

cal = MaxLimitCaculator()
cal.add(50)
cal.add(60)

print(cal.value)