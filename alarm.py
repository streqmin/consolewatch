import time
import threading
from datetime import datetime


class AlarmApp:
    class Alarm:
        def __init__(self):
            self._alarm_time = None
            self._message = None
        
        @property
        def alarm_time(self):
            return self._alarm_time
        
        @alarm_time.setter
        def alarm_time(self, time):
            self._alarm_time = time
        
        @property
        def message(self):
            return self._message
        
        @message.setter
        def message(self, message):
            self._message = message
        

    alarms = []
    
    def __init__(self):
        AlarmApp.alarms = []
        self.running = True
        threading.Thread(target=self.run, daemon=True).start()

    def add_alarm(self, hours, minutes, message):
        new_alarm = self.Alarm()
        
        alarm_time = datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0).time()
        
        new_alarm.alarm_time = alarm_time
        new_alarm.message = message
        
        AlarmApp.alarms.append(new_alarm)
        print(f"\n✅ 알람 추가됨: {alarm_time.strftime('%H:%M')} - {message}")

    def remove_alarm(self, index):
        if 0 <= index < len(AlarmApp.alarms):
            removed = AlarmApp.alarms.pop(index)
            print(f"\n🗑️ 알람 삭제됨: {removed.alarm_time.strftime('%H:%M')} - {removed.message}")
        else:
            print("\n❌ 잘못된 인덱스입니다.")

    def show_alarms(self):
        if not AlarmApp.alarms:
            print("\n⏳ 등록된 알람이 없습니다.")
            return False
        else:
            print("\n🔔 등록된 알람:")
            for i, alarm in enumerate(AlarmApp.alarms):
                print(f"{i + 1}. {alarm.alarm_time.strftime('%H:%M')} - {alarm.message}")
            return True

    def run(self):
        while self.running:
            now = datetime.now().time().replace(second=0, microsecond=0)  # 현재 시, 분만 비교
            for alarm in self.alarms[:]:
                if alarm.alarm_time == now:
                    print(f"\n⏰ [알람] {alarm.alarm_time.strftime('%H:%M')} - {alarm.message}")
                    self.alarms.remove(alarm)
            time.sleep(30)  # 초 단위 비교 대신 30초마다 체크하여 성능 최적화
