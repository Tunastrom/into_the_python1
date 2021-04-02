import re

def log_selector(backuplog_dict,needcolumns_dict, needconditions_set, rubbisies_set):
    needlog_list = []
    # get One row in all rows
    for key, row_dict in backuplog_dict.items():
        # row != 0 data rows
        if key != 0:
            # delete other datas in backuplog_dict that is not matched needcolumns_dict value columns 
            needrow_dict = dict()
            x = 0 
            check_result = 0
            for key, value in row_dict.items():
                k, v = key, value
                if k in needcolumns_dict.values():
                    print('v: {}'.format(v))
                    # Backup', '0', 'Default-Application-Backup' 포함하는 개수 체크
                    if v in needconditions_set:
                         check_result += 1     
                    # needlogs_list에 추가하기 전 임시 dictionary에 key, value 추가     
                    needrow_dict[x] = v
                    x+=1
            if check_result == 0:
                continue
            search_result = False
            # schedule명에 'full'포함되는 것만 needlog_list에추가
            if check_result == 2:
                policy_index = needcolumns_dict['JobSchedule']
                if row_dict[policy_index].find('full') != -1:
                    needlog_list.append(needrow_dict)
            # schedule명 Default Application Backup 인 것 중 full 백업만 needlog_list에추가
            if check_result == 3:
                policy_index = needcolumns_dict['JobPolicy']
                for search_this in rubbisies_set:
                    print(row_dict[policy_index])
                    if row_dict[policy_index].lower().find(search_this) != -1:
                        search_result = True
                        break
                if search_result is False:
                    needlog_list.append(needrow_dict)
        # row 0 column names
        elif key == 0:
            # Check the index of column which is needed to caculate backup amount 
            for key, value in row_dict.items():
                k, v = key, value
                if v in needcolumns_dict.keys():
                    needcolumns_dict.update({''+v:k})
            needlog_list.append(needcolumns_dict)
            print(needcolumns_dict.items())      
    for row in needlog_list:
        print(row) 
    print('---------------------------------------------------------------------------\n',len(needlog_list))