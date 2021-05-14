import re
import math


# 진행상황 표현
def percent_printer(percent, switch, checker):
    if percent % 10 == 0 and switch is True:
        if checker == 'date_split':
            print(f'날짜 공백 제거 {percent}% 완료')
        elif checker =='list_split':
            print(f'백업 로그 내 불필요 값 제거 진행률 {percent}%')
        elif checker == 'full_change':
            print(f'full 백업용량 수정 {percent}% 완료')
        elif checker == 'delete_row':
            print(f'backup기록 없는 서버 삭제 {percent}% 완료')
        return False
    elif percent % 10 > 0:
        return True


# 들어온 문자열의 내용 중에서 함께 가져온 정규표현식으로 검색되는 부분들의 공백제거후 string으로 반환
def string_splitter(pattern, string):
    input_str = string
    r = re.compile(pattern)
    search_result = r.search(input_str).group()
    while search_result:
        replaced_result = search_result.replace(' ', '')
        input_str = input_str.replace(search_result, replaced_result)
        try:
            # 정규표현식으로 들어온 문자열의 남은 부분 재검색
            search_result = r.search(input_str).group()
        except:
            # 정규표현식으로 검색되는 결과 없음.
            search_result = False
    return input_str


# 들어온 공백으로 구분된 행(문자열) 리스트의 요소를 공백제거 및 공백제거후 발생하는 ''요소들 제거후 dictionary형태로 반환
def row_list_split_into_dict(row_list):
    dictionary, i, switch, checker = {}, 0, bool, 'list_split'
    # 요소들 꺼내오기
    for row in row_list:
        row_element = row.split(' ')
        row_dict, j = {}, 0
        for alphabet in row_element:
            if alphabet != '':
                row_dict[j] = alphabet
                j += 1
        dictionary[i] = row_dict
        i += 1
        # 진행상황 표현
        now_count = row_list.index(row) + 1
        total_count = len(row_list)
        now_percent = math.floor((now_count / total_count) * 100)
        switch = percent_printer(now_percent, switch, checker)
    return dictionary


# xxxx특문xx특문xx 형태로 저장된 날짜를 year = xxxx, month = xx, day= xx 형태로 변환
def date_separator(date_str):
    pattern = '\d+'
    r = re.compile(pattern)
    year, month, day = 0, 0, 0
    try:
        for i in range(len(date_str)):
            if year != 0 and month != 0 and day != 0:
                break
            search_result = r.search(date_str).group()
            if i == 0:
                year = int(search_result)
                date_str = date_str.replace(search_result, '')
            if i == 1:
                month = int(search_result)
                date_str = date_str.replace('.{}.'.format(search_result), '')
            if i == 2:
                day = int(search_result)
                date_str = date_str.replace(search_result, '')
    except:
        year, month, day = 0, 0, 0
    return year, month, day
