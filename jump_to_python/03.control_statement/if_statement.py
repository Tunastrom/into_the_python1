print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('get on the taxi')
else:
    print('just walk')


if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

if 'money' in pocket: pass
else: print("카드를 꺼내라")  


score = 75

if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"
# <조건문이 참일 때> if <조건문> else <조건문이 거짓일 때>

