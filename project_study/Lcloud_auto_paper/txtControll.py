import re 

# Modify Colum names correclty 
Contents_str =''
with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102.txt', 'r') as f:
    Contents_str = f.read()
    pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
    search_result = re.search(pattern, Contents_str).group()
    while search_result:
        replaced_result = search_result.replace(' ','')
        Contents_str = Contents_str.replace(search_result,replaced_result)
        try:
            search_result=re.search(pattern, Contents_str).group()
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
    Contents_str = Contents_str.replace('Operation','')
    Contents_str = Contents_str.replace('StateDetails','')
    Contents_str = re.sub('[\w][\s][\w][\s][\d][\s][\D][\s][\w]', ' ', Contents_str,)  

with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102_rewrite.txt', 'w') as f:
    f.write(Contents_str)

with open('C:/Users/Administrator/Desktop/LCN_NBUActivity_202102_rewrite.txt', 'r') as f:
    Contents_list = f.readlines()
    # delete rubbish rows in Contents_list
    del Contents_list[0:7]
    del Contents_list[1]
    # make a Row_dict from a row and add it to a BackupLog_dict  
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
    # search and add into a dictionary
    BackupAmount_dict = {}
    OneRow_dict = {1:0, 2:0, 3:0, 4:'', 5:'', 6:0}
    NeedColums_dict = {'Type':0, 'Status':0, 'JobPolicy':0, 'JobSchedule':0, 'StartTime':0, 'Kilobytes':0}
    new_NeedCol_dict = {}
    ## Get BackupAmount from BackupLog_dict into the BackupAmount_dict
    # get One row in all rows
    y=1
    for key, Row_dict in BackupLog_dict.items():  
        # row != 0 data rows   
        if key != 0:
            # backup amount by cheking only NeedColums_dict value colums
            x = 0
            for key, value in Row_dict.items():
                k, v = key, value
                if k in NeedColums_dict.values():
                    OneRow_dict.update({x:v})
                    x+=1
            print(OneRow_dict.items(),'\n')              
            BackupAmount_dict.setdefault(y,OneRow_dict)
            # print(BackupAmount_dict.items())         
            y+=1      
        # row 0 colum names            
        elif key == 0:
            # Check the index of Colum which is needed to caculate backup amount 
            for key, value in Row_dict.items():
                k, v = key, value
                if v in NeedColums_dict.keys():
                    NeedColums_dict.update({''+v:k})
                    BackupAmount_dict.setdefault(0,NeedColums_dict)
            print(NeedColums_dict.items())      
    # for i in BackupAmount_dict.items():                
    #     print('------------------------------------------------------------------------\n')
    #     print(i,'\n')
                    
