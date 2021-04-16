def quiz():
    with open('vocabulary.txt', encoding='UTF-8') as file:
        for line in file.readlines():
            line_list = line.split(': ')
            kor = line_list[1].strip('\n')
            eng = line_list[0]
            answer = input(f'{kor}: ')
            if answer == eng:
                print('맞았습니다!')
            else:
                print(f'아쉽습니다. 정답은 {eng}입니다.')
quiz()