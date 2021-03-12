import os

os.chdir("C:/6000EC2_git/into_the_python1/jump_to_python")
f = os.popen("dir")
print(f.read())