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
# -> arguments are passed using call by value (wherer the )



#### parameter: formal parameter / actual parameter



