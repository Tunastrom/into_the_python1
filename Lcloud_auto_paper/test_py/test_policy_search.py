import os

def policy_search(policy_name):
    dir_path = 'C:/Users/flats/Desktop/PaperWorks/UWS_Docs/site_maintenance/2021/lotte/4/Lcloud/report/log/'
    for file_path in os.listdir(dir_path):
        with open(dir_path+file_path) as file:
            contents_list = file.readlines()
