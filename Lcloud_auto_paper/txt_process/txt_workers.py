import re
import os
import math
import datetime
import json

# Activity Monitor txt 파일 처리하는 메소드들


def pre_processor(txtpath, split_set, delete_set):
    print('전 처리 시작')
    # 전체 내용에서 단어 사이의 띄어쓰기 제거 및 값 없는 컬럼의 이름 삭제
    contents_str = ''
    with open(txtpath + '.txt', 'r') as f:
        contents_str = f.read()
        # start time 과 end time 공백제거
        date_pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
        contents_str = date_splitter(date_pattern, contents_str)
        print('컬럼 이름, 값 중간의 공백 제거')
        for name in split_set:
            splited_name = name.split(' ')
            contents_str = contents_str.replace(name, ''.join(splited_name))
        print('불필요한 컬럼 이름 삭제')
        for name in delete_set:
            contents_str = contents_str.replace(name, '')
    with open(txtpath + '_rewrite.txt', 'w') as f:
        f.write(contents_str)
        print('rewrite 완료')
    with open(txtpath + '_rewrite.txt', 'r') as f:
        contents_list = f.readlines()
        # 불필요한 행 삭제
        del contents_list[0:7]
        del contents_list[1]
        # 1개 행씩(row_dict) 읽어 공백제거 및 Backup_Log_dict에 요소로 추가
    backuplog_dict = row_split_into_dict(contents_list)
    # 사용완료한 rewrite 파일 삭제
    os.remove(txtpath + '_rewrite.txt')
    print('사용완료한 rewrite 파일 삭제')
    return backuplog_dict


def date_splitter(pattern, string):
    split_str = string
    r = re.compile(pattern)
    search_result = r.search(split_str).group()
    print('날짜 공백 제거 중')
    while search_result:
        replaced_result = search_result.replace(' ', '')
        split_str = split_str.replace(search_result, replaced_result)
        try:
            search_result = r.search(split_str).group()
        except:
            search_result = False
    os.system('cls')
    return split_str


def row_split_into_dict(contents_list):
    backuplog_dict = {}
    i = 0
    for row in contents_list:
        splited_row = row.split(' ')
        row_dict = {}
        j = 0
        for word in splited_row:
            if word != '':
                row_dict.setdefault(j, word)
                j += 1
        backuplog_dict.setdefault(i, row_dict)
        now_count = contents_list.index(row) + 1
        total_count = len(contents_list)
        now_percent = math.floor((now_count / total_count) * 100)
        print('로그 정리 진행률 {}%'.format(now_percent))
        if now_percent < 100:
            os.system('clear')
        i += 1
    return backuplog_dict


def full_selector(backuplog_dict,needcolumns_dict, needconditions_set, rubbisies_set):
    print('full backup 선별 중')
    fullbackups_list = []
    fullindexs_dict = {}
    policynames_list = []
    # fullbackup 정리 후의 컬럼이름과 값 index 매칭 정보 저장용 fullindexs_list 생성
    for key in needcolumns_dict:
        fullindexs_dict[key] = 0
    for key, row_dict in backuplog_dict.items():
        # 백업 로그들 하나씩 검색하여 성공한 full backup인지 확인 (needcolum_dict, needconditions_set, rubbisies_set 사용)
        if key != 0:
            needrow_dict = dict()
            x = 0
            check_result = 0
            # ImgClean = False
            for k, v in row_dict.items():
                for key, value in needcolumns_dict.items():
                    # neecolumns_dict에 저장된 index(value)와 일치하는 index의 값(v)들 needrow_dict에 순차 추가
                    if k == value:
                        # fullbackups_list의 컬럼명과 데이터가 매칭되는 index값 fullindexs_dict에 저장
                        fullindexs_dict[key] = x
                        # 'Backup', '0', 'Default-Application-Backup' 포함하는 개수 체크
                        if v in needconditions_set:
                            check_result += 1
                        # fullbackups_list에 추가하기 전 임시 dictionary에 key, value 추가
                        needrow_dict[x] = v
                        x += 1
            # full backup log가 아닐 때 다음행으로 넘어가기
            if check_result == 0 or check_result == 1:
                continue
            search_result = False
            # schedule명에 'full'포함되는 것만 fullbackups_list에추가
            if check_result == 2:
                policy_index = needcolumns_dict['JobSchedule']
                if row_dict[policy_index].find('full') != -1:
                    fullbackups_list.append(needrow_dict)
                    # job policy 이름 policynames_list에 추가
                    policynames_list.append(row_dict[needcolumns_dict['JobPolicy']])
            # schedule명 Default Application Backup 인 것 중 full 백업만 fullbackups_list에추가
            if check_result == 3:
                policy_index = needcolumns_dict['JobPolicy']
                for search_this in rubbisies_set:
                    if row_dict[policy_index].lower().find(search_this) != -1:
                        search_result = True
                        break
                if search_result is False:
                    fullbackups_list.append(needrow_dict)
                    # job policy 이름 policynames_list에 추가
                    policynames_list.append(row_dict[needcolumns_dict['JobPolicy']])
        # 필요한 컬럼명들의 index needcolums_dict의 value로 저장후 fullbackups_list의 0번째에 저장
        elif key == 0:
            # Check the index of column which is needed to caculate backup amount
            for key, value in row_dict.items():
                k, v = key, value
                if v in needcolumns_dict.keys():
                    needcolumns_dict.update({''+v:k})
            fullbackups_list.append(needcolumns_dict)
    fullbackups_list[0] = fullindexs_dict
    return fullbackups_list, policynames_list


def current_selector(fullbackups_list, policynames_list):

    one_time_fullbackup_dict = {}
    one_time_fullbackup_dict.setdefault('PolicyList', policynames_list)
    # policynames_list에 담긴 정책이름 for문 돌려서 날짜 가장 최근 것 검색한 뒤, 해당 날짜의 백업량 합 계산
    start_time_index, backupamount_index, policyname_index = \
        fullbackups_list[0]['StartTime'], fullbackups_list[0]['Kilobytes'], fullbackups_list[0]['JobPolicy']

    for policyname in policynames_list:
        timeandamount_dict = {}
        currenttime_date = datetime.date(2000, 2, 20)
        backupamount_int = 0
        print('--------------------------------------{}의 마지막 풀백업 수행날짜 및 용량 계산중------------------------------------'
              .format(policyname))
        for row in fullbackups_list:
            if fullbackups_list.index(row) == 0:
                continue
            if policyname == row[policyname_index]:
                # 2021.04.03 꼴의 날짜 값 search_result에 할당
                date_str = row[start_time_index]
                # 2021, 04, 03 꼴의 년, 월, 일값 각각 year, month, day에 할당
                year, month, day = date_separator(date_str)
                # 첫번째 StartTime currenttime_date으로 할당
                if fullbackups_list.index(row) == 0:
                    currenttime_date = datetime.date(year, month, day)
                    continue
                # 그 이후의 것들은 currenttime_date와 비교한 후 더 클때만 할당.
                comparing_time = datetime.date(year, month, day)
                if comparing_time > currenttime_date:
                    currenttime_date = comparing_time
                    timeandamount_dict.setdefault('Date', currenttime_date)
        one_time_fullbackup_dict.setdefault(policyname, timeandamount_dict)

        for row in fullbackups_list:
            if fullbackups_list.index(row) == 0:
                continue
            if policyname == row[policyname_index]:
                # print(row)
                pattern = '\d+[.]\d+[.]\d+'
                date_str = re.search(pattern, row[start_time_index]).group()
                currentdate_date = one_time_fullbackup_dict[policyname]['Date']
                year, month, date = date_separator(date_str)
                print('currentdate_date, datetime.date: {}, {}'
                      .format(currentdate_date, datetime.date(year, month, date)))
                if currentdate_date == datetime.date(year, month, date):
                    try:
                        print('row[backupamount_index]: {}'.format(row[backupamount_index]))
                        print('int(row[backupamount_index].replace(',
                              ', '')): {}'.format(int(row[backupamount_index].replace(',', ''))))
                        backupamount_int += int(row[backupamount_index].replace(',', ''))
                    except ValueError:
                        continue
            if type(currentdate_date) == datetime.date:
                one_time_fullbackup_dict[policyname]['Date'] = currentdate_date.strftime('%Y-%m-%d')
            print('backupamount_int: {}'.format(backupamount_int))
            one_time_fullbackup_dict[policyname]['Gigabyte'] = backupamount_int
    # 결과 프린트(확인용)
    for i in one_time_fullbackup_dict.items():
        print(i)

    return one_time_fullbackup_dict


def date_separator(date_str):
    pattern = '\d+'
    r = re.compile(pattern)
    year, month, day = 0, 0, 0
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
    return year, month, day


def make_summary_txt(txtpath, one_time_fullbackup_dict):
    one_time_fullbackup_str = json.dumps(one_time_fullbackup_dict)
    with open (txtpath+'_summary.txt', 'w') as f:
        f.write(one_time_fullbackup_str)

