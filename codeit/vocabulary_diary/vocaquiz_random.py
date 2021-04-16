import random

def dict_setter():
    with open('vocabulary.txt', encoding='UTF-8') as file:
        line_dict = {}
        line_list = file.readlines()
    for i in range(len(line_list)):
        line_dict[i] = line_list[i].strip().split(': ')
    return line_dict

def quiz(line_dict):
    line_len = len(line_dict)
    index = random.randint(0,(line_len-1))
    kor = line_dict[index][1]
    eng = line_dict[index][0]
    answer = input(f'{kor}: ')
    if answer == eng:
        print('맞았습니다!')
    elif answer == 'q':
        print('종료버튼을 누르셨습니다.')
        raise
    else:
        print(f'아쉽습니다. 정답은 {eng}입니다.')
    return True

line_dict = dict_setter()
switch = True
while switch:
    try:
        switch = quiz(line_dict)
        print('switch: {}'.format(switch))
    except:
        switch = False
        print('퀴즈를 종료합니다.')