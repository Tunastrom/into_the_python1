def average(*args):
    answer = 0
    for number in args:
        answer = answer + number
    return answer/len(args)

print(average(1,2,3,4,5,6,7,8,9,10))  