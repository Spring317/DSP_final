from new_recorder import recorder
from threading import Thread

run = recorder()

def Print():
    while True:
        print(run.difference, run.freq)

def run_record():
    run.record(196)

thread1 = Thread(target=run_record)
thread2 = Thread(target=Print)

thread1.start()
thread2.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

thread1.join()
thread2.join()
