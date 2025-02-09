import time
from stopwatch import Stopwatch
from alarm import AlarmApp


alarm = AlarmApp()
stopwatch = Stopwatch()

def handle_stopwatch():
    while True:
        print()
        key = input("명령어 입력 (s: 시작, q: 중지, r: 초기화, l: 랩 기록, e: 종료) > ").strip().lower()
        if   key == 's': stopwatch.start()
        elif key == 'q': stopwatch.stop()
        elif key == 'r': stopwatch.reset()
        elif key == 'l': stopwatch.record_lap()
        elif key == 'e':
            stopwatch.reset()
            print("프로그램을 종료합니다.")
            break
        else: print('\033[A\033[A\033[A')

def handle_alarm():
    while True:
        key = input("\n알람 관리 (a: 추가, v: 보기, d: 삭제, e: 종료) > ").strip().lower()
        if key == 'a':  # 알람 추가
            try:
                hours   = int(input("시간 (시): "))
                minutes = int(input("시간 (분): "))
                message = input("알람 메시지: ")
                alarm.add_alarm(hours, minutes, message)
            except ValueError:
                print("❌ 올바른 숫자를 입력하세요.")
        elif key == 'v':  # 알람 보기            
            alarm.show_alarms()
        elif key == 'd':  # 알람 삭제
            if alarm.show_alarms(): 
                try:
                    index = int(input("삭제할 알람 번호 입력: ")) - 1
                    alarm.remove_alarm(index)
                except ValueError:
                    print("❌ 올바른 숫자를 입력하세요.")
        elif key == 'e':  # 종료
            print("\n알람 관리 종료")
            break

def handle_timer():
    try:
        hours = int(input("시간 (시): ") or 0)
        minutes = int(input("시간 (분): ") or 0)
        seconds = int(input("시간 (초): ") or 0)
    except ValueError:
        print("❌ 올바른 숫자를 입력하세요.")
        return

    total_seconds = hours * 3600 + minutes * 60 + seconds
    print("\n⏳ 타이머 시작!")
    
    while total_seconds > 0:
        print(f"\r남은 시간: {total_seconds // 3600:02}:{(total_seconds % 3600) // 60:02}:{total_seconds % 60:02}", end="", flush=True)
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ 타이머 종료!")

def main():
    while True:
        print("\n📌 기능 선택")
        print("1: 스탑워치")
        print("2: 타이머")
        print("3: 알람 관리")
        print("4: 종료")
        choice = input("선택 (1/ 2/ 3/ 4): ").strip()

        if choice == "1":
            handle_stopwatch()
        elif choice == "2":
            handle_timer()
        elif choice == "3":
            handle_alarm()
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("❌ 올바른 번호를 입력하세요.")
            

if __name__ == "__main__":
    main()
