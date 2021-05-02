def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess) < 3:
        number_1 = input("{}번째 숫자를 입력하세요:".format(str(len(new_guess) + 1)))
        if number_1 >= 10:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif number_1 in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(number_1)
    # 코드를 작성하세요.

    return new_guess