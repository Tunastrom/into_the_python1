import re, datetime

def current_selector(fullbackups_list, needcolumns_dict, policynames_set):
    for row in fullbackups_list:
        print(row)
    print('---------------------------------------------------------------------------\n',len(fullbackups_list))
    print('policynames_set\n{}'.format(policynames_set))

    path ='\d+'
    r = re.compile(path)

    ## policynames_set에 담긴 정책이름 for문 돌려서 날짜 가장 최근 것 선택정렬 한 뒤, 해당 날짜의 백업량 합 계산
    start_time_index = fullbackups_list[0][needcolumns_dict['StartTime']]
    print('start_time_index: {}'.format(start_time_index))
    for policyname in policynames_set:
        for row in fullbackups_list: 
            print('policyname, row: {},{}'.format(policyname, row))
            if policyname in row.values():
                # 2021.04.03 꼴의 날짜 값 search_result에 할당 
                search_result = r.search(row[start_time_index]).group()
                year, month, day = '', '', ''
                # 2021, 04, 03 꼴의 년, 월, 일값 각각 year, month, day에 할당
                for i in range(len(search_result)):
                    if year != '' and month != '' and day != '':
                        break
                    if i == 0:
                        year = search_result
                        text = text.replace(search_result,'')
                    if i == 1:
                        month = search_result
                        text = text.replace(search_result,'')
                    if i == 2:
                        day = search_result
                        text = text.replace(search_result,'')
                # 첫번째 StartTime current_time으로 할당        
                if fullbackups_list.index(row) == 0:     
                   current_time = datetime.date(year, month, day)
                   continue
                # 그 이후의 것들은 current_time과 비교한 후 더 클때만 할당. 
                comparing_time = datetime.date(year, month, day)
                if comparing_time > current_time:
                    current_time = comparing_time 
               