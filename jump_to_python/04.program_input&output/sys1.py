# with open("foo.txt","w") as f:
#     f.write("Life is too short, you need python")

## sys module ##
# 명령 프롬프트 명령어 [인수1 인수2 ...]
# 매개변수를 직접 줄 수 있다.

import sys

args = sys.argv[1:]
           # 명령창에서 입력한 인수 
           # sys1.py   aaa     bbb     ccc
           # argv[0] argv[1] argv[2] argv[3]
for i in args:
    print(i)

