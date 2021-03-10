def average_all(*numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    average = total_sum / len(numbers)    
    return average

print(average_all(1,2,3,4,5,6,7,8,9,10))
