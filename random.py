import random
import time

while True:
    p = float(input("\n성공 확률을 입력하세요 (0~100, 종료는 -1): "))
    if p == -1:
        print("👋 프로그램 종료")
        break
    if not 0 < p <= 100:
        print("❌ 확률은 0보다 크고 100 이하여야 합니다.")
        continue

    repeat = int(input("반복할 횟수 입력: "))
    if repeat <= 0:
        print("❌ 반복 횟수는 1 이상이어야 합니다.")
        continue

    print_step = int(input("몇 회마다 성공 기록을 출력할까요? (0 = 출력 안 함): "))
    if print_step < 0:
        print("❌ 0 이상의 값을 입력하세요.")
        continue

    p /= 100
    results = []
    start = time.time()
    for _ in range(repeat):
        count = 0
        while True:
            count += 1
            if random.random() < p:
                results.append(count)
                if print_step != 0 and len(results) % print_step == 0:
                    print(f"{len(results)}: {count}번")
                break
    end = time.time()

    avg = sum(results) / len(results)

    avg_time = (end - start) / repeat
    
    print("\n📊 통계 결과")
    print(f"확률: {p*100}%")
    print(f"반복 횟수: {repeat}")
    print(f"총 소요 시간: {end - start:.2f}초")
    print(f"반복당 평균 시간: {avg_time*1000:.5f}ms")
    print(f"평균 시도 횟수: {avg:.2f}")
    print(f"최소: {min(results)}")
    print(f"최대: {max(results)}")
    print(f"이론적 평균: {1/p:.2f}")
