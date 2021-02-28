from itertools import permutations

def solution(numbers):  
    answer = ''
    numbers = list(map(str,numbers))
    f_numbers=set(i[0] for i in numbers)
    f_numbers=list(f_numbers)
    f_numbers.sort(reverse=True) #numbers안의 수(str)들 내림차순 정렬 
    highest_fnum = f_numbers[0]
    new_numbers=[]
    # numbers 안에 있는 수들의 첫째자리숫자 종류 만큼 list생성 후 new_numbers[]에 담기
    for i in range(len(f_numbers)):
        arr = []
        for j in numbers: 
            if str(j[0]) == f_numbers[i]:
                arr.append(j)  
        new_numbers.append(arr)
    # 가장 큰 수 찾아내기
    thousand = 0
    for x in new_numbers:
        if x == 1000:
            thousand = 1000
        # 첫째자리수가 중복되는 다른 수 없으면 answer에 더하기     
        elif len(x) == 1:
            answer += x[0]
        # 첫째자리수 중복인 다른 수 있으면 가장 값이 큰 조합 찾아 answer에 더하기         
        elif len(x) >= 2:
            # test = list(permutations(x, len(x)))
            # print(test[0][0])
            x_list = ["".join(z) for z in list(permutations(x, len(x))) if z[0] == highest_fnum ]
            print(x_list)
            x_list = list(map(int,x_list))
            x_list.sort(reverse=True)
            answer += str(x_list[0])             
    if thousand == 1000: 
        answer += thousand         