import tempfile

filename = tempfile.mkstemp()
                   # 무작위로 생성된, 이름이 중복되지 않는 임시파일 생성해 반환
print(filename)

f = tempfile.TemporaryFile()
            # 임시저장공간으로 사용할 파일객체 반환
f.close()
# close() 호출시 위 파일 객체 자동으로 삭제
 
