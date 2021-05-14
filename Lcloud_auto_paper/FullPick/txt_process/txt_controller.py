from .txt_workers import *

def txt_controller(PATHDIR,TXTPATH):

    PATH = PATHDIR+TXTPATH

    # 작업에 불필요한 컬럼명들
    DELETE_SET={  
            'Operation', 'State Details', 'copy', 'Robot', 'Vault', 'Profile', 'Session ID', 'Media to Eject', 'Data Movement', 'Instance or Database',
            'Share Host', 'Accelerator Optimization', 'Master', 'Priority', 'Transport', 'Pathname'
    }

    # 문자열 안의 공백 없애야 할 컬럼명 정의 
    SPLIT_SET={
            'Job Id', 'Job Policy', 'Job Schedule', 'Start Time', 'Elapsed Time', 'End Time', 'Media Server', 'Storage Unit', 'Off-Host Type',
            'Image Cleanup', 'Catalog Backup', '% Complete (Estimated)', 'Job PID', 'Parent Job ID', 'Active Start', 'Active Elapsed', 'Deduplication Rate'
    }

    # 작업에 필요한 컬럼명 정의
    NEEDCOLUMNS_DICT = {'Type':0, 'Status':0, 'Client':0 ,'JobPolicy':0, 'JobSchedule':0, 'StartTime':0, 'Kilobytes':0}

    # 필요한 데이터 정의(추가적인 연산 필요)
    NEEDCONDITIONS_SET = {'Backup', '0', 'Default-Application-Backup'}

    # 불필요한 데이터 정의
    RUBBISIES_SET = {'tran', 'inc', 'arc'}


    print(f"+++++++++++++++++++++++++++++++++++{TXTPATH} 작업시작++++++++++++++++++++++++++++++++++++++++")

    # 컬럼명 행 요소([0])와 데이터 행 요소([1]~[n])의 value에 저장된 dictionary의 key값이 서로 매칭된 행(dict)들을 요소로 갖는 backuplog_dict 반환
    backuplog_dict = pre_processor(PATH, SPLIT_SET, DELETE_SET)
    
    # backuplog_dict에서 성공한 full백업만 추출해 fullbackups_list에 append하여 반환
    fullbackups_list, policynames_list = full_selector(backuplog_dict, NEEDCOLUMNS_DICT, NEEDCONDITIONS_SET, RUBBISIES_SET)
    
    # policy별로 가장 최근의 full백업 찾아내 1회 풀백업 용량 계산
    one_time_fullbackup_dict = current_selector(fullbackups_list, policynames_list)

    print(f"+++++++++++++++++++++++++++++++++++{TXTPATH} 작업완료++++++++++++++++++++++++++++++++++++++++")

    # 완성된 결과파일 새 txt파일에 쓰고 완성된 one_time_fullbackup_dict 반환
    return make_summary_txt(PATH, one_time_fullbackup_dict)





