import re 

# 전체 내용에서 단어 사이의 띄어쓰기 제거 및 값 없는 컬럼의 이름 삭제 
Contents_str =''
with open('C:/Users/Administrator/Desktop/test_log/Export1_ext.txt', 'r') as f:
    Contents_str = f.read()
    # start time 과 end time 공백제거  
    pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
    r = re.compile(pattern)
    search_result = r.search(Contents_str).group()
    while search_result:
        replaced_result = search_result.replace(' ','')
        Contents_str = Contents_str.replace(search_result,replaced_result)
        try:
            search_result=r.search(Contents_str).group()
        except:
            search_result = False
    
    split_set={
        'Job Id','Job Policy','Job Schedule','Start Time','Elapsed Time','End Time','Media Server','Storage Unit','Off-Host Type',
        'Image Cleanup', 'Catalog Backup', '% Complete (Estimated)','Job PID', 'Parent Job ID', 'Active Start', 'Active Elapsed', 'Deduplication Rate'
    }
    delete_set={ 
        'Operation', 'State Details', 'copy', 'Robot', 'Vault', 'Profile', 'Session ID', 'Media to Eject', 'Data Movement', 'Instance or Database',
        'Share Host', 'Accelerator Optimization', 'Master', 'Priority', 'Transport', 'Pathname'
    }
    
    for name in split_set:
        splited_name = name.split(' ')
        Contents_str = Contents_str.replace(name,''.join(splited_name))

    for name in delete_set:
        Contents_str = Contents_str.replace(name,'')
    
    # # 전체 내용중 
    # Contents_str = re.sub('[\w][\s][\w][\s][\d][\s][\D][\s][\w]', ' ', Contents_str)  

with open('C:/Users/Administrator/Desktop/test_log/Export1_ext_rewrite.txt', 'w') as f:
    f.write(Contents_str)

with open('C:/Users/Administrator/Desktop/test_log/Export1_ext_rewrite.txt', 'r') as f:
    Contents_list = f.readlines()
    # 불필요한 행 삭제 
    del Contents_list[0:7]
    del Contents_list[1]
    # 1개 행씩(Row_dict) 읽어 공백제거 및 Backup_Log_dict에 요소로 추가    
    BackupLog_dict = {}
    i = 0
    for row in Contents_list:
        splited_row = row.split(' ')
        Row_dict  = { }
        j = 0
        for word in splited_row:
            if word != '':
                Row_dict.setdefault(j,word)
                j += 1
        BackupLog_dict.setdefault(i, Row_dict)
        Row_dict={}
        i += 1
    # print(len(BackupLog_dict.items())) 
    # 필요한 컬럼명과 걸러내야할 데이터들 정의
    NeedLogs_dict = {}
    Needcolumns_dict = {'Type':0, 'Status':0, 'Client':0 ,'JobPolicy':0, 'JobSchedule':0, 'StartTime':0, 'Kilobytes':0}
    RubbishDatas_set = {'CatalogBackup', 'ImageCleanup', 'Archive', 'incre', ''}
    new_NeedCol_dict = {}
    ## full backup log들의 필요한 컬럼만 추려낸 새로운 행을 NeedLogs에 요소로 추가 
    y=1
    # get One row in all rows
    for key, Row_dict in BackupLog_dict.items():  
        # row != 0 data rows
        if key != 0:
            # delete other datas in BackupLog_dict that is not matched Needcolumns_dict value columns 
            OneRow_dict = dict()
            x = 0 
            for key, value in Row_dict.items():
                k, v = key, value
                # print(k, v, '\n')
                if k in Needcolumns_dict.values():
                    OneRow_dict[x] = v
                    x+=1
            # print(OneRow_dict.items(),'\n')
            NeedLogs_dict.setdefault(y,OneRow_dict)
            # print(len(NeedLogs_dict.items()))           
            y+=1      
        # row 0 column names            
        elif key == 0:
            # Check the index of column which is needed to caculate backup amount 
            for key, value in Row_dict.items():
                k, v = key, value
                if v in Needcolumns_dict.keys():
                    Needcolumns_dict.update({''+v:k})
                    NeedLogs_dict.setdefault(0,Needcolumns_dict)
            print(Needcolumns_dict.items())      
    print('---------------------------------------------------------------------------\n',len(NeedLogs_dict.items()))
    for key,value in NeedLogs_dict.items():
        print(key,value)
    
                    
