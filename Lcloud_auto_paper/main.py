import sys, time
sys.path.append('C:/6000EC2_git/into_the_python1/Lcloud_auto_paper/text_process')
from text_process.text_controller import *

def main():
    start_time = time.time()
    text_controller()
    end_time = time.time()
    spend_time = end_time - start_time
    print('spend time: {}'.format(spend_time))

if __name__ == "__main__":
     main()

