from text_process.pre_processor import *
from text_process.log_selector import *


def text_controller():
    # 삭제해야할 컬럼명 정의 

    txtpath = 'C:/Users/Administrator/Desktop/test_log/LCN_NBUActivity_202102'

    delete_set={  
            'Operation', 'State Details', 'copy', 'Robot', 'Vault', 'Profile', 'Session ID', 'Media to Eject', 'Data Movement', 'Instance or Database',
            'Share Host', 'Accelerator Optimization', 'Master', 'Priority', 'Transport', 'Pathname'
    }

    # 문자열 안의 공백 없애야 할 컬럼명 정의 
    split_set={
            'Job Id', 'Job Policy', 'Job Schedule', 'Start Time', 'Elapsed Time', 'End Time', 'Media Server', 'Storage Unit', 'Off-Host Type',
            'Image Cleanup', 'Catalog Backup', '% Complete (Estimated)', 'Job PID', 'Parent Job ID', 'Active Start', 'Active Elapsed', 'Deduplication Rate'
    }

    # 필요한 컬럼명 정의
    needcolumns_dict = {'Type':0, 'Status':0, 'Client':0 ,'JobPolicy':0, 'JobSchedule':0, 'StartTime':0, 'Kilobytes':0}

    # 필요한 데이터 정의
    needconditions_set = {'Backup', '0', 'Default-Application-Backup'}

    # 불필요한 데이터 정의

    rubbisies_set = { 'tran', 'inc', 'arc' }
    
    # 컬럼명 행과 데이터 행의 key값이 서로 매칭된 행(dict)들을 요소로 갖는 backuplog_dict 반환 
    backuplog_dict = pre_processor(txtpath, split_set, delete_set, needcolumns_dict)
    
    # backuplog_dict에서 필요한 컬럼만 추출해 needlog_list에 append하여 반환
    needlog_list = log_selector(backuplog_dict, needcolumns_dict, needconditions_set, rubbisies_set )