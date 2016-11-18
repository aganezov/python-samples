# -*- coding: utf-8 -*-

import threading
import time


lock = threading.Lock()


def print_time(name, counter, delay):
    while counter > 0:
        time.sleep(delay)
        print("{name} {time}".format(name=name, time=time.ctime(time.time())))
        counter -= 1
        time.sleep(delay)


class JBGWUThread(threading.Thread):
    def __init__(self, thread_id, name, lock, counter=None, delay=3):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.lock = lock
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Staring {name} {time}".format(name=self.name, time=time.ctime(time.time())))
        # THE STUFF
        with self.lock:
            print_time(self.name, self.counter, self.delay)
        # THE STUFF has ended...
        print("Exiting {name} {time}".format(name=self.name, time=time.ctime(time.time())))


thread1 = JBGWUThread(1, "JBGWUThread1", counter=3, delay=4, lock=lock)
thread2 = JBGWUThread(2, "JBGWUThread2", counter=5, delay=2, lock=lock)



thread1.start()
time.sleep(.2)
thread2.start()
print("Exiting Main {time}".format(time=time.ctime(time.time())))

