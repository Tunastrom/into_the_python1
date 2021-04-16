from random import randint


def generate_numbers():
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = set()

    while True:
        numbers.add(randint(0, 9))
        numbers_len = len(numbers)
        if numbers_len == 3:
            break

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return list(numbers)


def take_guess():
    # 지난 과제의 코드를 붙여 넣으세요.
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    index = 0

    while len(new_guess) < 3:
        value = int(input(f'{index+1}번째 숫자를 입력하세요: '))
        if value < 0 or value > 9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        elif value in new_guess:
            print('중복된 숫자입니다. 다시 입력하세요')
        else:
            new_guess.append(value)
            index += 1

    return new_guess


def get_score(guess, solution):
    # 지난 과제의 코드를 붙여 넣으세요.
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요

while True:
    tries += 1
    strike_count, ball_count = get_score(take_guess(), ANSWER)
    print(f'{strike_count}S {ball_count}B')
    if strike_count == 3:
        break


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
