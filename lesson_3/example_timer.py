import time


def run_work(delay):
    print("I am sleeping")
    time.sleep(delay)


start = time.time()
run_work(3)
stop = time.time()

print(f"Work time {start - stop}")
