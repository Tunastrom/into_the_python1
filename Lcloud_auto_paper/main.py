from txt_process.txt_controller import *
import sys
import time

sys.path.append('/txt_process')

def main():
    start_time = time.time()
    TXTPATH = 'C:/Users/Administrator/Desktop/test_log/2021.Mar/global_psmgtbms01'
    text_controller(TXTPATH)
    end_time = time.time()
    spend_time = end_time - start_time
    print('spend time: {}'.format(spend_time))

if __name__ == "__main__":
     main()

