while number := input("0~1000사이의 정수를 입력하세요\n"):  # 사용자의 입력을 받아
    if number.isdigit() is False or int(number) > 1000: # 타입체크
        continue
    print(f'입력값: {number}')
    break

total, sum_to_total = 1, 2 # 누적합을 담을 변수와 1부터 1씩 늘어나는 덧셈용 변수
while number:
    if total >= int(number): # 누적합이 사용자의 입력값과 같거나 큰지 체크 후 작업종료
        print(f'마지막에 더한 정수: {sum_to_total-1}')
        number = False
    else:
        total += sum_to_total # 누적합
        sum_to_total += 1





