
def log_selector(backuplog_dict,needcolumns_dict):
    needlogs_list = []
    new_needcol_dict = {}
    # get One row in all rows
    for key, row_dict in backuplog_dict.items():
        # row != 0 data rows
        if key != 0:
            # delete other datas in backuplog_dict that is not matched needcolumns_dict value columns 
            needrow_dict = dict()
            x = 0 
            for key, value in row_dict.items():
                check_result = 0
                k, v = key, value 
                # print(k, v, '\n')
                if k in needcolumns_dict.values():
                    if v in ['Backup', '0', 'full', 'Default-Application-Backup']:
                         check_result += 1  
                    needrow_dict[x] = v
                    x+=1               
            # print(needrow_dict.items(),'\n')
            if check_result == 4:
                needlogs_list.append(needrow_dict)
            # print(len(needlogs_list.items()))                
        # row 0 column names            
        elif key == 0:
            # Check the index of column which is needed to caculate backup amount 
            for key, value in row_dict.items():
                k, v = key, value
                if v in needcolumns_dict.keys():
                    needcolumns_dict.update({''+v:k})
                    needlogs_list.append(needcolumns_dict)
            print(needcolumns_dict.items())      
    for row in needlogs_list:
        print(row) 
    print('---------------------------------------------------------------------------\n',len(needlogs_list))        