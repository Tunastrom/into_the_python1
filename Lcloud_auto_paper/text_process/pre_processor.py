from .date_splitter import date_splitter
import re,os,math


def pre_processor(txtpath, split_set, delete_set, needcolumns_dict):  
    print('전 처리 시작')
    # 전체 내용에서 단어 사이의 띄어쓰기 제거 및 값 없는 컬럼의 이름 삭제 
    contents_str = ''
    with open(txtpath+'.txt', 'r') as f:
        contents_str = f.read()
        # start time 과 end time 공백제거
        date_pattern = '\d+[.][ ]\d+[.][ ]\d+[ ]\D+[ ]\d+[:]\d+[:]\d+'
        contents_str = date_splitter(date_pattern, contents_str)
        print('컬럼 이름, 값 중간의 공백 제거')
        for name in split_set:
            splited_name = name.split(' ')
            contents_str = contents_str.replace(name,''.join(splited_name))
        print('불필요한 컬럼 이름 삭제')
        for name in delete_set:
            contents_str = contents_str.replace(name,'')
     
    with open(txtpath+'_rewrite.txt', 'w') as f:
        f.write(contents_str)
        print('rewrite 완료')

    with open(txtpath+'_rewrite.txt', 'r') as f:
        contents_list = f.readlines()
        # 불필요한 행 삭제
        del contents_list[0:7]
        del contents_list[1]
        # 1개 행씩(row_dict) 읽어 공백제거 및 Backup_Log_dict에 요소로 추가   
    backuplog_dict = row_split_into_dict(contents_list)
    
    os.remove(txtpath+'_rewrite.txt')

    return backuplog_dict
    

def row_split_into_dict (contents_list):
    backuplog_dict = {}
    i = 0
    for row in contents_list:
        splited_row = row.split(' ')
        row_dict  = {}
        j = 0
        for word in splited_row:
            if word != '':
                row_dict.setdefault(j,word)
                j += 1
        backuplog_dict.setdefault(i, row_dict)
        now_count = contents_list.index(row)+1
        total_count= len(contents_list)
        now_percent = math.floor((now_count/total_count)*100)
        print('로그 정리 진행률 {}%'.format(now_percent))
        if now_percent < 100:
            os.system('cls')
        i += 1
    # print(len(backupLog_dict.items()))
    return backuplog_dict   

    