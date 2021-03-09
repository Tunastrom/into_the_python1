
import os
### 환경변수,디렉토리,파일 등의 OS자원을 제어하는 모듈

## 내 시스템의 환경변수 값 출력
# print(os.environ)
# print(os.environ['path'])


## 디렉토리 위치 지정 
os.chdir('c:\\WINDOWS')

## 디렉토리 위치 출력
print(os.getcwd())

## 시스템 명령어 호출
os.system('dir')
# = cmd에서 dir 입력

## 실행한 시스템 명령어의 결과값 반환
f = os.popen('dir')
print(f.read())
# read도 되네??

## 그외
# os.mkdir('directory name')
# os.rmdir('directory name')
# os.unlink('file name')
# os.rename('src', 'dst')
# 파일 src의 이름을 dst로 바꿈
# 

