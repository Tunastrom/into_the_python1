
numbers = [1,2,4,9,90,900,909,1000]
f_numbers = ['1','2','4','9']
new_numbers = []

for i in range(len(f_numbers)):
    arr = []
    for x in numbers:
        print('x: '+str(x))
        if str(x)[0] == f_numbers[i]:
            arr.append(str(x))
            print('arr: ', arr)
    new_numbers.append(arr)
    print(new_numbers)

            세 자리 수 중 둘째자리 >= 첫째자리인 수 빼내어 배열 추가 & 내림차순 정렬 
            for i in x:
                # print('here',x)
                if len(i) == 3:
                    
                    big_list.append(x.pop(x.index(i)))    
            big_list = list(map(int,big_list))
            big_list.sort(reverse=True)
            answer += "".join(list(map(str,big_list)))
            

# 두 자리 수 중 둘째자리 >= 첫째자리인 수 빼내 배열추가 후 내림차순 정렬
            for i in x:
                if len(i) == 2 and i[1] >= i[0]:
                    if i[1] != 0:
                        big_list.append(x.pop(x.index(i)))
                    # 단 둘째자리가 0이면 리스트에 그대로 둠
                    elif i[1] == 0:
                        continue   
            big_list=list(map(int,big_list))
            big_list.sort(reverse=True)
            answer += "".join(list(map(str,big_list)))
            big_list.clear()
