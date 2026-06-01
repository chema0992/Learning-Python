import time
import os
import pygame

version = '1.0.6 - ERROR DEBUG 1'

print(f"Py Jump Rope Counter ver.{version}")
print("Program Exit: Enter the -1")

# 1. 오디오 시스템 초기화 (동시 재생 채널 확보)
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# 도, 레, 미 소리 파일 이름 (프로그램과 같은 폴더에 있어야 합니다)
sound_files = ["do.mp3", "re.mp3", "mi.mp3"]
sounds = []

# 파일이 실제로 존재하는지 체크하고 불러오기
for f in sound_files:
    if os.path.exists(f):
        sounds.append(pygame.mixer.Sound(f))
    else:
        print(f"⚠️ 경고: '{f}' 파일이 폴더에 없습니다! 소리가 나지 않을 수 있습니다.")
        # 파일이 없을 때 에러 방지용 가짜 객체 넣기
        sounds.append(None)

# 2. 사용자 입력 및 무한 루프
while True:
    jump_type = input("원하는 점프 종류를 입력하세요 (번갈아 / 이중): ")
    if jump_type == '-1':
        break
        
    n = float(input("30초 동안 몇 개를 뛸 건가요? (숫자만): "))
    if n == -1:
        break

    if jump_type == "번갈아":
        interval = 30.0 / (n * 2)
        stack_use = input("오른발 / 전체 중 카운트 할 것을 선택해주세요 : ")

        if stack_use == '오른발':
            stack_use = 1
        else:
            stack_use = 0
    else:
        stack_use = 0
        interval = 30.0 / n

    print("▶️ 3초 후 측정을 시작합니다...")
    time.sleep(3)

    # 3. 메인 타이머 루프
    start_time = time.time()
    next_play_time = interval
    count = 0
    stack = 0

    print("🏁 시작!")
    while True:
        current_time = time.time() - start_time
        
        if current_time >= 30.0:
            break
            
        if current_time >= next_play_time:
            
            stack += 1
            
            if stack_use == 0:
                count += 1
                sound_index = (count - 1) % 3
                
                # 🔊 [실제 소리 재생 코드] 
                # .play()를 실행하면 이전 소리가 안 끝나도 겹쳐서 재생됩니다! (개사기 기능)
                if sounds[sound_index] is not None:
                    sounds[sound_index].play()
                notes = ["도 🔴", "레 🟢", "미 🔵"]
                print(f"[{current_time:.2f}초] {notes[sound_index]} (카운트: {count})")
            else:
                if stack == 2:
                    count += 1
                    sound_index = (count - 1) % 3
                    
                    # 🔊 [실제 소리 재생 코드] 
                    # .play()를 실행하면 이전 소리가 안 끝나도 겹쳐서 재생됩니다! (개사기 기능)
                    if sounds[sound_index] is not None:
                        sounds[sound_index].play()
                        
                    print(f"[{current_time:.2f}초] 쾅! (카운트: {count})")
                    stack = 0
            next_play_time += interval
            
        time.sleep(0.001)

    print("\n⏱️ 30초 종료! 수고하셨습니다.")
