import re
import math
import datetime

# Activity Monitor txt 파일 처리하는 메소드들
def pre_processor(TXTPATH, SPLIT_SET, DELETE_SET):
    print('=============================================전 처리 시작===================================================')
    # 전체 내용에서 단어 사이의 띄어쓰기 제거 및 값 없는 컬럼의 이름 삭제
    contents_str = ''
    with open(TXTPATH + '.txt', 'r') as f:
        contents_list = f.readlines()
        # start time 과 end time 공백제거
        date_pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
        print('<날짜 공백 제거 시작>')
        switch = False
        for line in contents_list:
            try:
                # 날짜 공백 제거함수 수행 후 결과 새로운 문자열에 추가
                contents_str += string_splitter(date_pattern, line)
            except AttributeError:
                # 날짜가 없는 행은 그대로 추가
                contents_str += line
            # 날짜 공백 제거 진행률 표현
            percent = round((contents_list.index(line) / len(contents_list)) * 100)
            if percent % 10 == 0 and switch is True:
                print('날짜 공백 제거 {}% 완료'.format(percent))
                switch = False
            elif percent % 10 > 0:
                switch = True
        print('<컬럼 이름, 값 중간의 공백 제거>')
        for name in SPLIT_SET:
            splited_name = name.split(' ')
            contents_str = contents_str.replace(name, ''.join(splited_name))
        print('<불필요한 컬럼 이름 삭제>')
        for name in DELETE_SET:
            contents_str = contents_str.replace(name, '')
        # 전체 내용을 \n을 기준으로 나누어 각 행을 요소로 갖는 리스트 만들기
        contents_list = contents_str.split('\n')
        # 불필요한 행 삭제
        del contents_list[0:7]
        del contents_list[1]
    # 1개 행씩(row_dict) 읽어 공백제거 및 Backup_Log_dict에 요소로 추가
    print('<백업 로그 내 불필요 값 제거>')
    backuplog_dict = list_split_into_dict(contents_list)
    return backuplog_dict

# 들어온 문자열의 내용 중에서 함께 가져온 정규표현식으로 검색되는 부분들의 공백제거후 string으로 반환
def string_splitter(pattern, string):
    split_str = string
    r = re.compile(pattern)
    search_result = r.search(split_str).group()
    while search_result:
        replaced_result = search_result.replace(' ', '')
        split_str = split_str.replace(search_result, replaced_result)
        try:
            search_result = r.search(split_str).group()
        except:
            # 정규표현식으로 검색되는 결과 없음.
            search_result = False
    return split_str

# 들어온 문자열 리스트의 요소를 공백제거 및 공백제거후 발생하는 ''요소들 제거후 dictionary형태로 반환
def list_split_into_dict(string_list):
    backuplog_dict = {}
    i = 0
    switch = bool
    # 요소들 꺼내오기
    for element in string_list:
        splited_element = element.split(' ')
        row_dict = {}
        j = 0
        for word in splited_element:
            if word != '':
                row_dict[j] = word
                j += 1
        backuplog_dict[i] = row_dict
        now_count = string_list.index(element) + 1
        total_count = len(string_list)
        now_percent = math.floor((now_count / total_count) * 100)
        if now_percent % 10 == 0 and switch is True:
            print('백업 로그 내 불필요 값 제거 진행률 {}%'.format(now_percent))
            switch = False
        elif now_percent % 10 > 0:
            switch = True
        i += 1

    return backuplog_dict


def full_selector(backuplog_dict,NEEDCOLUMNS_DICT, NEEDCONDITIONS_SET, RUBBISIES_SET):
    print('==============================================full backup 선별 시작=========================================================')
    fullbackups_list = []
    fullindexs_dict = {}
    policynames_set = set()
    # fullbackup 정리 후의 컬럼이름과 값 index 매칭 정보 저장용 fullindexs_list 생성
    for key in NEEDCOLUMNS_DICT:
        fullindexs_dict[key] = 0
    for key, row_dict in backuplog_dict.items():
        # 백업 로그들 하나씩 검색하여 성공한 full backup인지 확인 (needcolum_dict, NEEDICONDITIONS_SET, RUBBISIES_SET 사용)
        if key != 0:
            needrow_dict = dict()
            x = 0
            check_result = 0
            for k, v in row_dict.items():
                for key, value in NEEDCOLUMNS_DICT.items():
                    # needcolumns_dict에 저장된 index(value)와 일치하는 index의 값(v)들 needrow_dict에 순차 추가
                    if k == value:
                        # fullbackups_list의 컬럼명과 데이터가 매칭되는 index값 fullindexs_dict에 저장
                        fullindexs_dict[key] = x
                        # 'Backup', '0', 'Default-Application-Backup' 포함하는 개수 체크
                        if v in NEEDCONDITIONS_SET:
                            check_result += 1
                        # fullbackups_list에 추가하기 전 임시 dictionary에 key, value 추가
                        needrow_dict[x] = v
                        x += 1
            # full backup log가 아닐 때 다음행으로 넘어가기
            if check_result == 0 or check_result == 1:
                continue
            # Full Backup 정책인지 아닌지 체크해 fullbackups_list에 추가
            search_result = False
            if check_result == 2:
                kilobytes = NEEDCOLUMNS_DICT['Kilobytes']
                policy_index = NEEDCOLUMNS_DICT['JobPolicy']
                schedule_index = NEEDCOLUMNS_DICT['JobSchedule']
                search_result = policy_checker(RUBBISIES_SET, row_dict[kilobytes], row_dict[policy_index], row_dict[schedule_index])
                if search_result is False:
                    fullbackups_list.append(needrow_dict)
                    # job policy 이름 policynames_set에 추가
                    policynames_set.add(row_dict[NEEDCOLUMNS_DICT['JobPolicy']])
            # schedule명 Default Application Backup 인 것 중 full 백업만 fullbackups_list에추가
            if check_result == 3:
                kilobytes = NEEDCOLUMNS_DICT['Kilobytes']
                policy_index = NEEDCOLUMNS_DICT['JobPolicy']
                search_result = policy_checker(RUBBISIES_SET, row_dict[kilobytes], row_dict[policy_index])
                if search_result is False:
                    fullbackups_list.append(needrow_dict)
                    # job policy 이름 policynames_set에 추가
                    policynames_set.add(row_dict[NEEDCOLUMNS_DICT['JobPolicy']])
        # 필요한 컬럼명들의 index needcolums_dict의 value로 저장후 fullbackups_list의 0번째에 저장
        elif key == 0:
            # Check the index of column which is needed to caculate backup amount
            for key, value in row_dict.items():
                k, v = key, value
                # print('k, v: {}, {}'.format(k, v))
                if v in NEEDCOLUMNS_DICT.keys():
                    NEEDCOLUMNS_DICT.update({''+v:k})
            fullbackups_list.append(NEEDCOLUMNS_DICT)
    fullbackups_list[0] = fullindexs_dict
    # for line in fullbackups_list:
    #      print(f'<fullbackups_list> {line}')
    return fullbackups_list, list(policynames_set)


# 정책명에 tran, arc, inc 포함되어 있는지, file backup일 경우 schedule명에 'full' 있는 지 까지 체크
def policy_checker(*args):
    rubbish = False
    # Kilobytes 행에 백업용량이 아닌 다른 값이 들어왔을 때 해당 job 걸러내기
    try:
        int(''.join(args[1].split(',')))
    except:
         rubbish = True
         return rubbish
    if len(args) == 3:
        # schedule 이름이 Default-Application-Backup일때 policy name에 tran, inc, arc 들어간 것 찾아내 해당 job 걸러내기
        for search_this in args[0]:
            if args[2].lower().find(search_this) != -1:
                rubbish = True
                return rubbish
    elif len(args) == 4:
        # file backup 중 schedule 이름에 full 들어가지 않은 것 찾아내 해당 job 걸러내기
        if rubbish is False and args[3].lower().find('full') == -1:
            rubbish = True
    return rubbish


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
        print('<{}의 마지막 풀백업 수행날짜 및 용량>'
              .format(policyname))
        # 마지막 full backup 날짜 계산
        for row in fullbackups_list:
            currentdate_date = ''
            if fullbackups_list.index(row) == 0:
                continue
            if policyname == row[policyname_index]:
                # 2021.04.03 꼴의 날짜 값 search_result에 할당
                date_str = row[start_time_index]
                # 2021, 04, 03 꼴의 년, 월, 일값 각각 year, month, day에 할당
                year, month, day = date_separator(date_str)
                # print ('year, month, day: {}, {}, {}'.format(year, month, day))
                if year == 0 or month == 0 or day == 0:
                    continue
                # 첫번째 StartTime currenttime_date으로 할당
                if fullbackups_list.index(row) == 0:
                    currenttime_date = datetime.date(year, month, day)
                    continue
                # 그 이후의 것들은 currenttime_date와 비교한 후 더 클때만 할당.
                comparingtime_date = datetime.date(year, month, day)
                if comparingtime_date > currenttime_date:
                    currenttime_date = comparingtime_date
                    timeandamount_dict.setdefault('Date', currenttime_date)
        print(f'current_start: {timeandamount_dict["Date"]}')
        one_time_fullbackup_dict[policyname] = timeandamount_dict
        # 마지막 full backup 수행일자의 백업용량 계산
        for row in fullbackups_list:
            if fullbackups_list.index(row) == 0:
                continue
            # 현재 작업중인 정책명과 읽어들인 행의 정책명을 비교해 일치하는 것 찾기
            if policyname == row[policyname_index]:
                pattern = '\d+[.]\d+[.]\d+'
                # 현재 행의 start 날짜 가져오기
                try:
                    date_str = re.search(pattern, row[start_time_index]).group()
                except:
                    # 에러 발생시엔 필요없는 행(ex. kilobyte 컬럼 공백)이므로 다음 행으로 이동
                    continue
                # 현재 작업중인 정책의 최신 start 날짜 가져오기
                currentdate_date = one_time_fullbackup_dict[policyname]['Date']
                # currentdate_date의 타입이 datetime.date일 때만 현재 행의 날짜를 date_saperator에 보내 year, month, date로 분해
                if type(currentdate_date) == datetime.date:
                    year, month, date = date_separator(date_str)
                # 분해된 현재 행의 start 날짜를 datetime.date 타입으로 바꾸어 최신날짜와 비교
                if currentdate_date == datetime.date(year, month, date):
                    # 최신날짜와 같으면 backupamount_int에 누적
                    try:
                        backupamount_int += int(row[backupamount_index].replace(',', ''))
                    except ValueError:
                        continue
        print(f'backupamount_int: {backupamount_int}')
        # 현재 작업중인 정책의 최신날짜가 datetime.date타입(xxxx.xx.xx)이면 xxxx-xx-xx형태로 변환
        if type(currentdate_date) == datetime.date:
             one_time_fullbackup_dict[policyname]['Date'] = currentdate_date.strftime('%Y-%m-%d')
        # 현재 작업중인 정책의 최신날짜 기준 백업용량을 Gigabyte단위로 환산해 저장
        gigabyte = round(backupamount_int/1024/1024, 2)
        # 현재 작업중인 정책의 최신날짜 기준 백업용량이 1기가 미만이라면 1기가로 올려서 저장
        if 0 <= gigabyte and gigabyte < 1:
             gigabyte = 1
        one_time_fullbackup_dict[policyname]['Gigabyte'] = gigabyte
    # 결과 프린트(확인용)
    print('===============================================1회 full backup 계산 완료!=====================================================')
    for i in one_time_fullbackup_dict.items():
        print(i)

    return one_time_fullbackup_dict

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
        pass
    return year, month, day

# 완성된 정책별 최신 풀백업 수행날짜 및 풀백업 용량을 .txt 파일로 저장
def make_summary_txt(TXTPATH, one_time_fullbackup_dict):

    # one_time_fullbackup_str = json.dumps(one_time_fullbackup_dict)
    write_list = []
    for item in one_time_fullbackup_dict.items():
        write_list.append(item)
    with open (TXTPATH+'_summary.txt', 'w') as f:
        for line in write_list:
           f.write(str(line))
           f.write('\n')
    print('<'+TXTPATH+'_summary.txt 파일이 생성되었습니다!>')
    return one_time_fullbackup_dict


