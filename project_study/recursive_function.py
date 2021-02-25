### recursive function

def factorial(n):

    if (n == 1):
        return 1
    
    return n * factorial(n-1)

print(factorial(3))

def recursion_sum(n,m):

    if m >= n:
        return m + recursion_sum(n,m-1)
    else:
        return 0

 
## tail recursion - saving resorces, but same looping times and time complexity

def tail_recursion_sum(total, n, m):

    if m >= n:
        return tail_recursion_sum(total + m, n, m-1)
    else:
        return total
  
## loop  

def loop_sum(n,m):

    total = 0 
    while m >= n:
        total += m
        m -= 1

    return total