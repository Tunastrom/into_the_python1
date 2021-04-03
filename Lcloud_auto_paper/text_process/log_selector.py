import re

def log_selector(backuplog_dict,needcolumns_dict, needconditions_set, rubbisies_set):
    fullbackups_list = []
    fullindexs_dict = {}
    policynames_set = set()
    # fullbackup 정리 후의 컬럼이름과 값 index 매칭 정보 저장용 fullindexs_list 생성
    for key in needcolumns_dict:
        fullindexs_dict[key] = 0
    print('fullindexs_dict: {}'.format(fullindexs_dict))
    # get One row in all rows
    for key, row_dict in backuplog_dict.items():
        # row != 0 data rows
        if key != 0:
            # delete other datas in backuplog_dict that is not matched needcolumns_dict value columns 
            needrow_dict = dict()
            x = 0
            check_result = 0
            ImgClean = False
            for k, v in row_dict.items():
                if v == 'ImageCleanup':
                    ImgClean = True
                for key, value in needcolumns_dict.items():
                    # neecolumns_dict에 저장된 index(value)와 일치하는 index의 값(v)들 needrow_dict에 순차 추가
                    if k == value:
                        # fullbackups_list의 컬럼명과 데이터가 매칭되는 index값 fullindexs_dict에 저장
                        fullindexs_dict[key] = x    
                        # 'Backup', '0', 'Default-Application-Backup' 포함하는 개수 체크
                        if v in needconditions_set:
                            check_result += 1
                        # needlogs_list에 추가하기 전 임시 dictionary에 key, value 추가
                        needrow_dict[x] = v
                        x += 1
                        # job policy 이름들 set에 추가해 전체 종류 구함   
                        if k == needcolumns_dict['JobPolicy']:
                            if ImgClean is True:
                                ImgClean = False
                                continue   
                            print ('k, index: {}, {}'.format(k, needcolumns_dict['JobPolicy']))
                            policynames_set.add(v)
            # 'Backup', '0', 'Default-Application-Backup' 중 포함하는 것 없을 때 다음행으로 넘어가기
            if check_result == 0:
                continue
            search_result = False
            # schedule명에 'full'포함되는 것만 fullbackups_list에추가
            if check_result == 2:
                policy_index = needcolumns_dict['JobSchedule']
                if row_dict[policy_index].find('full') != -1:
                    fullbackups_list.append(needrow_dict)
            # schedule명 Default Application Backup 인 것 중 full 백업만 fullbackups_list에추가
            if check_result == 3:
                policy_index = needcolumns_dict['JobPolicy']
                for search_this in rubbisies_set:
                    if row_dict[policy_index].lower().find(search_this) != -1:
                        search_result = True
                        break
                if search_result is False:
                    fullbackups_list.append(needrow_dict)
        # 필요한 컬럼명들의 index needcolums_dict의 value로 저장후 fullbackups_list의 0번째에 저장
        elif key == 0:
            # Check the index of column which is needed to caculate backup amount 
            for key, value in row_dict.items():
                k, v = key, value
                if v in needcolumns_dict.keys():
                    needcolumns_dict.update({''+v:k})
            fullbackups_list.append(fullindexs_dict)

    return fullbackups_list, policynames_set 
        

       
     
