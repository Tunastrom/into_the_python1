def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(reverse=True)
    # print(numbers)  
    combi=[]
    for i in numbers:
        count=0
        for j in numbers: 
            if j.startswith(i[0]) == True:
                count+=1         
        if count >= 2:    
            combi.append(i)    
            combination.add(set(combi))
    print(combination)