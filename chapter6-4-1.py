# Chapter6-4-1
# 파이썬 심화
# Asynco
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 stop -> 다른 작업으로 위임 -> Stop 지점부터 재실행 원리
# Non-Blocking 비동기 처리 적합

# Block I/O
# 순차 실행

import timeit
from urllib.request import urlopen

urls = ['https://www.google.com', "https://www.apple.com", "https://www.naver.com", "https://github.com", "https://www.fastcampus.co.kr/"]

start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print("Start", url)
    # 실제 요청
    text = urlopen(url)
    # 실제 내용
    # print("Content", text.read())
    print("Done", url)

# 완료 시간 - 시작시간
duration = timeit.default_timer() - start

# 총 실행 시간
print("Total Time", duration)