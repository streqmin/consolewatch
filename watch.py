import time
import threading
from datetime import datetime

class Alarm:
    def __init__(self):
        self.alarms = []
        self.running = True
        threading.Thread(target=self.run, daemon=True).start()

    def add_alarm(self, hours, minutes, seconds, message):
        alarm_time = datetime.now().replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
        if alarm_time < datetime.now():  # 이미 지난 시간이면 내일로 설정
            alarm_time = alarm_time.replace(day=datetime.now().day + 1)

        self.alarms.append((alarm_time, message))
        print(f"\n✅ 알람 추가됨: {alarm_time.strftime('%H:%M:%S')} - {message}")

    def remove_alarm(self, index):
        if 0 <= index < len(self.alarms):
            removed = self.alarms.pop(index)
            print(f"\n🗑️ 알람 삭제됨: {removed[0].strftime('%H:%M:%S')} - {removed[1]}")
        else:
            print("\n❌ 잘못된 인덱스입니다.")

    def show_alarms(self):
        if not self.alarms:
            print("\n⏳ 등록된 알람이 없습니다.")
        else:
            print("\n🔔 등록된 알람:")
            for i, (time, message) in enumerate(self.alarms):
                print(f"{i + 1}. {time.strftime('%H:%M:%S')} - {message}")

    def run(self):
        while self.running:
            now = datetime.now().replace(microsecond=0)
            for alarm in self.alarms[:]:
                if alarm[0] <= now:
                    print(f"\n⏰ [알람] {alarm[0].strftime('%H:%M:%S')} - {alarm[1]}")
            time.sleep(1)

class Stopwatch:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = 0.0
        self.lap_times = []

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            print("\n⏳ 스탑워치 시작!", end="", flush=True)
            threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        while self.running:
            elapsed = time.time() - self.start_time
            print(f"\r경과 시간: {elapsed:.2f} 초", end="", flush=True)
            time.sleep(0.1)

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print(f"\n🛑 스탑워치 중지. 총 경과 시간: {self.elapsed_time:.2f} 초")
        else: print('🛑 스탑워치가 실행 중이 아닙니다.', end='')

    def reset(self):
        self.running = False
        self.elapsed_time = 0.0
        self.lap_times = []
        print("\n♻ 스탑워치 초기화됨.")

    def record_lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.lap_times.append(lap_time)
            print(f"\n🏁 랩 {len(self.lap_times)} 기록: {lap_time:.2f} 초")

alarm = Alarm()

def handle_stopwatch():
    stopwatch = Stopwatch()
    while True:
        key = input("\n명령어 입력 (s: 시작, q: 중지, r: 초기화, l: 랩 기록, e: 종료) > ").strip().lower()
        if key == 's':
            stopwatch.start()
        elif key == 'q':
            stopwatch.stop()
        elif key == 'r':
            stopwatch.reset()
        elif key == 'l':
            stopwatch.record_lap()
        elif key == 'e':
            print("\n프로그램을 종료합니다.")
            break

def handle_alarm():
    while True:
        key = input("\n알람 관리 (a: 추가, v: 보기, d: 삭제, e: 종료) > ").strip().lower()
        if key == 'a':  # 알람 추가
            try:
                hours = int(input("시간 (시): "))
                minutes = int(input("시간 (분): "))
                seconds = int(input("시간 (초): "))
                message = input("알람 메시지: ")
                alarm.add_alarm(hours, minutes, seconds, message)
            except ValueError:
                print("❌ 올바른 숫자를 입력하세요.")
        elif key == 'v':  # 알람 보기
            alarm.show_alarms()
        elif key == 'd':  # 알람 삭제
            alarm.show_alarms()
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
        hours = int(input("시간 (시): "))
        minutes = int(input("시간 (분): "))
        seconds = int(input("시간 (초): "))
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
