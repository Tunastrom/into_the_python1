import os


def str_into_txt():
    eng = input('영어 단어를 입력하세요: ')
    if(eng == 'q'):
        raise
    kor = input('한국어 뜻을 입력하세요: ')
    if(kor == 'q'):
        raise
    try:
        with open('vocabulary.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{eng}: {kor}\n')
    except:
        with open('vocabulary.txt', 'w', encoding='UTF-8') as file:
            file.write(f'{eng}: {kor}\n')
    return True


run_switch = True
while run_switch:
    try:
        run_switch = str_into_txt()
    except:
        run_switch = False