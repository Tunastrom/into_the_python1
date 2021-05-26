import os
import time
from FullPick import txt_process, xlsx_process


def main():
    start_time = time.time()
    txt_path_dir = 'C:/Users/flats/Desktop/PaperWorks/UWS_Docs/site_maintenance/2021/lotte/5/Lcloud/report/log/'
    xlsx_path_dir = 'C:/Users/flats/Desktop/PaperWorks/UWS_Docs/site_maintenance/2021/lotte/5/Lcloud/report/'
    # pdf_path_dir = '~~~~'
    txt_name_list = os.listdir(txt_path_dir)
    for txt_name in txt_name_list:
        # try:
            if txt_name.lower().find('policy') == -1 and txt_name.lower().find('summary') == -1:
                print(txt_name)
                one_time_fullbackup_dict = txt_process.txt_controller(txt_path_dir, txt_name)
                xlsx_process.xlsx_controller(one_time_fullbackup_dict, xlsx_path_dir)
                print()
        # except:
        #     print()
        #     continue
    # pdf_process.pdf_controller()
    end_time = time.time()
    spend_time = end_time - start_time
    print('spend time: {}'.format(spend_time))


if __name__ == "__main__":
     main()

