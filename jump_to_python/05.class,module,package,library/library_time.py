import time

print(time.time())
# UTC(Universal Time Coordinated 협정세계표준시)를 사용해 현재시간을 실수형식으로 반환
# 1970.01.01 00:00:00 기준으로 현재까지 경과된 시간 초단위 반환

print(time.localtime(time.time()))
# time.time()이 반환한 실수값을 연도,월,일,시,분,초의 형태로 바꾸어 반환


print(time.asctime(time.localtime(time.time())))
# time.localtime()이 반환한 튜플 형식의 값을 받아 날짜와 시간을 알아보기 쉽게 변환해 반환

print(time.strftime('%a', time.localtime(time.time())))
# 시간을 세밀하게 표현하는 여러 포멧코드를 사용해 더 세밀하게 다룰 수있다.

## format code ##

#참조: https://wikidocs.net/33

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))
# 3.9에선 그냥 localtime과 차이가 없다. 
print(time.strftime('%c',time.localtime(time.time())))

# 일정 시간 간격(sleep(interval))을 두고 loop 실행
for i in range(10):
    print(i)
    time.sleep(1)

