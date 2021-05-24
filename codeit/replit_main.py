import os


# input 메소드
def input_checker():
    input_checker = False
    while input_checker == False:
        try:
            print('[숫자 입력]')
            select_num = int(input(': ')) - 1
            os.system('clear')
            input_checker = True
        except ValueError:
            print('!!숫자를 입력하세요!!\n[숫자 입력]')
        except IndexError:
            print('!!주어진 선택지 안의 수를 입력하세요!!\n[숫자입력]')
    return select_num


def main(dir_name):
    if dir_name == '':
        # 멤버별 디렉토리명 찾아서 members list에 추가
        members = list()
        for name in os.listdir('/home/runner/02-forsentence/project/'):
            if name != '.upm' and name != 'main.py':
                members.append(name)

        # members list에 있는 멤버이름들 input_massage에 추가하고 출력
        input_massage = str()
        for i in range(len(members)):
            input_massage += f'{i + 1}. {members[i]}\n'
        print(f'__실행할 멤버을 선택하세요__\n\n{input_massage}')

        # 실행할 멤버 선택받기
        select_num = input_checker()
        dir_name, select_num = members[select_num], 0

    # 선택한 멤버의 python 파일 files list에 추가
    print(f'__{dir_name}의 python 파일__')
    files = list()
    for name in os.listdir(f'project/{dir_name}'):
        files.append(name)

    # files list에 있는 멤버이름들 input_massage에 추가하고 출력
    input_massage = str()
    if len(files) == 0:
        print('\n!!실행할 파일이 없습니다!!\n')
        return dir_name

    for i in range(len(files)):
        input_massage += f'{i + 1}. {files[i]}\n'
    print(f'\n{input_massage}')

    # 선택한 멤버의 python 파일들 중에서 실행할 파일 선택
    select_num = input_checker()
    py_name, select_num = files[select_num], 0
    print(f'<{py_name}>')
    print(f'----------------------------------------------------------------\n')

    # 선택한 python file 실행
    os.system(f'python project/{dir_name}/{py_name}')

    print(f'\n----------------------------------------------------------------\n')
    return dir_name


# 프로그램 제어용 변수 설정
exit_switch, dir_name = False, ''

# 프로그램 시작
while exit_switch == False:
    # 멤버선택 후 해당 멤버가 작성한 python 파일 실행
    dir_name = main(dir_name)
    print(f'{dir_name}님의 python 파일을 계속 실행하시겠습니까?\n1. yes\n2. no\n')
    select_num = input_checker()
    if select_num == 1:
        print('다른 멤버의 python 파일을 검색하시겠습니까?\n1. yes\n2. no\n')
        select_num = input_checker()
        # dir_name의 값을 ''로 바꾸어 main() 내에서 dir_name 입력받게 설정
        if select_num == 0:
            dir_name = ''
        # exit_switch의 값을 True로 바꾸어 프로그램 종료
        elif select_num == 1:
            exit_switch = True
print('프로그램을 종료합니다.')
