while dices := tuple((input("주사위 A와 B의 면 수를 공백을 넣어서 입력하세요\n")).split()):  # 사용자의 입력을 받아
    dice_a, dice_b = dices
    if dice_a.isdigit() is False or int(dice_a) > 10 \
    or dice_b.isdigit() is False or int(dice_b) > 10: # 타입체크
        continue
    print(f'입력값: {dices}')
    break

for number_a in range(1,int(dice_a)+1):
    for number_b in range(1,int(dice_b)+1):
        print(number_a, number_b)
