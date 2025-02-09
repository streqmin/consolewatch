import time
import threading


class Stopwatch:
    running = False
    lap_times = 0
    start_time = None
    elapsed_time = 0.0

    def start(self):
        if Stopwatch.running:
            print("\033[A\033[A\033[A\r")
        else: 
            Stopwatch.running = True
            Stopwatch.start_time = time.time() - Stopwatch.elapsed_time
            print("\n⏳ 스탑워치 시작!", flush=True)
            threading.Thread(target=self.run, daemon=True).start()

    def run(self):
        while Stopwatch.running:
            time.sleep(0.1)
            elapsed = time.time() - Stopwatch.start_time
            # print(f"\033[A\r경과 시간: {elapsed:.2f} 초\033[B\033[{n}G", end="", flush=True)
            print(f"\033[A\r경과 시간: {elapsed:.2f} 초\033[B", end="", flush=True)

    def stop(self):
        if Stopwatch.running:
            Stopwatch.elapsed_time = time.time() - Stopwatch.start_time
            Stopwatch.running = False
            print(f"\n🛑 스탑워치 중단. 현재 경과 시간: {Stopwatch.elapsed_time:.2f} 초")
        else: 
            print('🛑 스탑워치가 실행 중이 아닙니다.', end='')

    def reset(self):
        Stopwatch.running = False
        Stopwatch.elapsed_time = 0.0
        Stopwatch.lap_times = 0
        print("\n♻ 스탑워치 초기화됨.")

    def record_lap(self):
        if Stopwatch.running:
            lap_time = time.time() - Stopwatch.start_time
            Stopwatch.lap_times += 1
            print(f"\n🏁 랩 {Stopwatch.lap_times} 기록: {lap_time:.2f} 초")