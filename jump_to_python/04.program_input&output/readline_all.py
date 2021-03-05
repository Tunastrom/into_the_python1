f = open("c:\새파일.txt", 'r')
while True:
    line = f.readline() # 파일의 첫번째 줄부터 1줄 읽음 
    if not line: break
    print(line)
f.close()

# while 1:
#     data = input()
#     if not data: break
#     print(data)


f = open("c:\새파일.txt", 'r')
lines = f.readlines()
       # 파일의 모든 라인을 읽어서 각 줄을 요소로 갖는 리스트로 반환
for line in lines:
    print(line)
f.close()


f = open("c:\새파일.txt", 'r')
data = f.read()
       # 파일의 전체 라인을 문자열로 반환
print(data)
f.close()
