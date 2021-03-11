
import sys

argv = sys.argv

def myargv(val):
    total = 0
    for i in val: 
        if val.index(i) == 0: continue
        else: total += int(i)
    return total

print(myargv(argv))    
    