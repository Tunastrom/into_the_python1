def fib(n): # -> n = formal parameter
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
fib(2000) # -> 2000 actual parameter

# def + <function name> + parenthesized list of formal parameters

# make a habit of writing docstrings 

# execution of a function introduces a nwe symbol table used for the local variables of the fucntion

# sequence of referencing variables
# local symbol table -> local symbol tables of enclosing function -> global symbol table -> table of built-in name
#         1                                 2                                  3                      4         
#                       ***** can not assign the value directly to these variables *****       
# 
 
# The actual parameters to a function call are introduced in the local symbol table of the called function when it is called
# -> arguments are passed using call by value (where the value is always an object reference, not the value of the object).

#### parameter: formal parameter / actual parameter

# When a funcion calls another function or calls itself recursively, a new local symbol table is created for that call.

# A function definition associates the function name with the function object in the current symbol table. 
# The interpreter recognizes the object pointed to by that name as a user-defined function.
# Other names can also point to that same function object and can also be used to access the function

# In python, even functions without a return statement do return a value.
# This value is called None. = built-in name
# If it would be the only value written, it is suppressed by Interpreter 
# but can see that by using print()

print(fib)
f = fib
print(f(100))

print(fib(0))


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

