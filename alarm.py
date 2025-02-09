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