
def append_to_file():
    f = open('test.txt', 'a')
    f.write(input('추가할 값을 입력하세요'))
    f.close()


append_to_file()
v = open('test.txt', 'r')
print(v.read())

