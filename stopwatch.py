import time
import threading


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
            print("\n⏳ 스탑워치 시작!", flush=True)
            threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        time.sleep(0.1)
        while self.running:
            elapsed = time.time() - self.start_time
            # print(f"\033[A\r경과 시간: {elapsed:.2f} 초\033[B\033[{n}G", end="", flush=True)
            print(f"\033[A\r경과 시간: {elapsed:.2f} 초\033[B", end="", flush=True)
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