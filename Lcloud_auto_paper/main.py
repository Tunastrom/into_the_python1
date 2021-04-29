import os
import time
import datetime

from pdf_process.pdf_controller import pdf_controller
from txt_process.txt_controller import txt_controller
from xlsx_process.xlsx_controller import xlsx_controller


def main():
    start_time = time.time()
    # print(datetime.date.now)
    path_dir = "C:/Lcloud_auto_paper/activitylogs_txt/202104/"
    path_list = os.listdir(path_dir)
    for txt_path in path_list:
        if txt_path.lower().find('policy') == -1 and txt_path.lower().find('summary') == -1:
            print(txt_path)
            txt_controller(path_dir, txt_path)
            print()
    # xlsx_controller(one_time_fullbackup_dict)
    end_time = time.time()
    spend_time = end_time - start_time
    print('spend time: {}'.format(spend_time))


if __name__ == "__main__":
     main()

