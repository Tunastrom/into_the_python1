#break, else

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equeals', x, '*', n//x)
            break
    else: 
        # excuted when the loop terminates through exhaustion of the iterable  
        # or when the condition becomes false
        # but not when the loop is terminated by a break statement
        print(n , 'is a prime number')

#continue

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num) 

# pass

while True:
    pass

class MyEmptyClass:
    pass


def initlog(*args):
    pass