# Chapter6-3-1
# 파이썬 심화
# Future 동시성
# 비동기 작업 실행
# 지연시간(Block), CPU 및 리소스 낭비 -> Network I/O 관련 작업 동시성 활용 권장
# 적합한 작업일 경우 순차 진행보다 압도적으로 성능 향상

# 실습 3가지

# 순차 실행
# concurrent.futures 방법1
# concurrent.futures 방법2

import os
import time
import sys
import csv

# 순차 실행 예제

# 국가 정보
NATION_LS = ('Singapore Germany Israel Norway Italy Canada France Spain Mexico').split()
# 초기 CSV 위치
TARGET_CSV = "./resources/nations.csv"
# 저장 폴더 위치
DEST_DIR = "./csvs"
# CSV 헤더 정보
HEADER = ['Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date','Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']

# 국가별 CSV 파일 저장
def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    with open(path, "w", newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)
        # Header Write
        writer.writeheader()
        # Dict -> CSV Write
        for row in data:
            writer.writerow(row)


# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict -> List
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data


# 상황 출력
def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 비우기)
    sys.stdout.flush()


# 국가별 분리 함수 실행
def separate_many(nt_list):
    for nt in sorted(nt_list):
        # 분리 데이터
        data = get_sales_data(nt)
        # 상황 출력
        show(nt)
        # 파일 저장
        save_csv(data, nt.lower() + '.csv')

    return len(nt_list)


def main(separate_many):
    # 시작 시간
    start_time = time.time()
    # 결과 건수
    result_cnt = separate_many(NATION_LS)
    # 종료 시간
    end_time = time.time() - start_time

    msg = "\n{} csv separated in {:.2f}s"

    print(msg.format(result_cnt, end_time))

# 실행
if __name__ == "__main__":
    main(separate_many)