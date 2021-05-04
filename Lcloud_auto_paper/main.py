import os
import time
import datetime
import txt_process
import pdf_process
import xlsx_process


def main():
    start_time = time.time()
    # print(datetime.date.now)
    path_dir = "C:/Lcloud_auto_paper/activitylogs_txt/202104/"
    path_list = os.listdir(path_dir)
    # for txt_path in path_list:
    #     if txt_path.lower().find('policy') == -1 and txt_path.lower().find('summary') == -1:
    #         print(txt_path)
    #         txt_process.txt_controller(path_dir, txt_path)
    #         print()
    pdf_process.pdf_controller()
    # xlsx_controller(one_time_fullbackup_dict)

    end_time = time.time()
    spend_time = end_time - start_time
    print('spend time: {}'.format(spend_time))


if __name__ == "__main__":
     main()

