import random

# 코드를 작성하세요.
correct_answer = random.randint(1,21)
print(correct_answer)


opertunity, game_on = 4, True
while game_on is True:
    if opertunity == 0:
        print(f'아쉽습니다. 정답은 {correct_answer}입니다.')
        game_on = False
        continue
    user_answer = input(f'기회가 {opertunity}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ')
    if type(int(user_answer)) == int:
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print(f'축하합니다. {5 - opertunity}번 만에 숫자를 맞히셨습니다.')
            game_on = False
            continue
        elif  user_answer > correct_answer and opertunity > 0:
            print('Down')
            opertunity -= 1
            continue
        elif  user_answer < correct_answer and opertunity > 0:
            print('Up')
            opertunity -= 1
            continue
    else:
        print('숫자를 입력하세요!')
        continue