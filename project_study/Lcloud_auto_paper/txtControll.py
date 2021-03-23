import re 

# 컬럼 이름의 띄어쓰기 제거 및 값 없는 컬럼 삭제 
Contents_str =''
with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102.txt', 'r') as f:
    Contents_str = f.read()
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

    Contents_str = Contents_str.replace('Job Id','JobId')
    Contents_str = Contents_str.replace('Job Policy','JobPolicy') 
    Contents_str = Contents_str.replace('State Details','StateDetails')
    Contents_str = Contents_str.replace('Job Schedule','JobSchedule')
    Contents_str = Contents_str.replace('Start Time','StartTime')
    Contents_str = Contents_str.replace('Elapsed Time','ElapsedTime')   
    Contents_str = Contents_str.replace('End Time','EndTime')
    Contents_str = Contents_str.replace('Media Server','MediaServer')
    Contents_str = Contents_str.replace('Storage Unit','StorageUnit')
    Contents_str = Contents_str.replace('Off-Host Type','Off-HostType')
    Contents_str = Contents_str.replace('Image Cleanup','ImageCleanup')
    Contents_str = Contents_str.replace('Catalog Backup','CatalogBackup')
    Contents_str = Contents_str.replace('Operation','')
    Contents_str = Contents_str.replace('StateDetails','')
    # 데이터 비어있는 컬럼이름들 추가적인 삭제 필요
    Contents_str = re.sub('[\w][\s][\w][\s][\d][\s][\D][\s][\w]', ' ', Contents_str,)  

with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102_rewrite.txt', 'w') as f:
    f.write(Contents_str)

with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102_rewrite.txt', 'r') as f:
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
    Needcolumns_dict = {'Type':0, 'Status':0, 'JobPolicy':0, 'JobSchedule':0, 'StartTime':0, 'Kilobytes':0}
    RubbishDatas_set = set({'CatalogBackup', 'ImageCleanup'})
    new_NeedCol_dict = {}
    ## 필요한 컬럼만 추려낸 새로운 행을 NeedLogs에 요소로 추가 
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
            # print(Needcolumns_dict.items())      
    print('---------------------------------------------------------------------------\n',len(NeedLogs_dict.items()))
    for key,value in NeedLogs_dict.items():
        print(key,value)
    
                    
