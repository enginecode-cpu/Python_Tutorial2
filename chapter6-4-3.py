# Chapter6-4-3
# 파이썬 심화
# Asynco
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 stop -> 다른 작업으로 위임 -> Stop 지점부터 재실행 원리
# Non-Blocking 비동기 처리 적합

# Block I/O -> Thread 사용
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결
# 순차 실행

# aiohttp 사용 가능(Asyncoio 지원)
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import asyncio

urls = ['https://www.google.com', "https://www.apple.com", "https://www.naver.com", "https://github.com", "https://www.fastcampus.co.kr/"]

start = timeit.default_timer()

async def fetch(url, executor):
    print("Thread Name : ", threading.current_thread().getName(), "Start", url)
    # result = await urlopen(url) # Error
    result = await loop.run_in_executor(executor, urlopen, url)
    print("Thread Name : ", threading.current_thread().getName(), "Done", url)
    return result.read()[:5]

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # asyncoio.ensure_future
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    result = await asyncio.gather(*futures)

    print()
    # 결과 확인
    print("Result : ", result)



if __name__ == "__main__":
    # 루프 생성
    loop = asyncio.get_event_loop()
    # 루프 대기
    loop.run_until_complete(main())
    # 함수 실행
    main()
    # 완료 시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print("Total Time", duration)