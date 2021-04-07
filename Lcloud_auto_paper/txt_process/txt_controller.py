from txt_process.txt_workers import *






def text_controller():
    # 삭제해야할 컬럼명 정의 

    TXTPATH = 'C:/Users/Administrator/Desktop/test_log/2021.Mar/global_psmgtbms01'

    DELETE_SET={  
            'Operation', 'State Details', 'copy', 'Robot', 'Vault', 'Profile', 'Session ID', 'Media to Eject', 'Data Movement', 'Instance or Database',
            'Share Host', 'Accelerator Optimization', 'Master', 'Priority', 'Transport', 'Pathname'
    }

    # 문자열 안의 공백 없애야 할 컬럼명 정의 
    SPLIT_SET={
            'Job Id', 'Job Policy', 'Job Schedule', 'Start Time', 'Elapsed Time', 'End Time', 'Media Server', 'Storage Unit', 'Off-Host Type',
            'Image Cleanup', 'Catalog Backup', '% Complete (Estimated)', 'Job PID', 'Parent Job ID', 'Active Start', 'Active Elapsed', 'Deduplication Rate'
    }

    # 필요한 컬럼명 정의
    NEEDCOLUMNS_DICT = {'Type':0, 'Status':0, 'Client':0 ,'JobPolicy':0, 'JobSchedule':0, 'StartTime':0, 'Kilobytes':0}

    # 필요한 데이터 정의
    NEEDCONDITIONS_SET = {'Backup', '0', 'Default-Application-Backup'}

    # 불필요한 데이터 정의
    RUBBISIES_SET = { 'tran', 'inc', 'arc'}
    
    # 컬럼명 행과 데이터 행의 key값이 서로 매칭된 행(dict)들을 요소로 갖는 backuplog_dict 반환 
    backuplog_dict = pre_processor(TXTPATH, SPLIT_SET, DELETE_SET)
    
    # backuplog_dict에서 성공한 full백업만 추출해 fullbackups_list에 append하여 반환
    fullbackups_list, policynames_list = full_selector(backuplog_dict, NEEDCOLUMNS_DICT, NEEDCONDITIONS_SET, RUBBISIES_SET)
    
    # policy별로 가장 최근의 full백업 찾아내 1회 풀백업 용량 계산
    one_time_fullbackup_dict = current_selector(fullbackups_list, policynames_list)

    # 완성된 결과파일 새 txt파일에 쓰기
    make_summary_txt(TXTPATH, one_time_fullbackup_dict)
