import sys
import time

from pdf_process.pdf_controller import pdf_controller
from txt_process.txt_controller import txt_controller
from xlsx_process.xlsx_controller import xlsx_controller


def main():
    start_time = time.time()
    txt_path = 'C:/Lcloud_auto_paper/activitylogs_txt/202103/global_mgt-ext-backup'
    txt_controller(txt_path)
    # one_time_fullbackup_dict = txt_controller(txt_path)
    # xlsx_controller(one_time_fullbackup_dict)
    end_time = time.time()
    spend_time = end_time - start_time
    print('spend time: {}'.format(spend_time))


if __name__ == "__main__":
     main()

