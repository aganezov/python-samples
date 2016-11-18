# -*- coding: utf-8 -*-

import threading
import time


def print_time(name, counter, delay):
    while counter > 0:
        time.sleep(delay)
        print("{name} {time}".format(name=name, time=time.ctime(time.time())))
        counter -= 1
        time.sleep(delay)


























class JBGWUThread(threading.Thread):
    def __init__(self, thread_id, name, counter=None, delay=3):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Staring {name} {time}".format(name=self.name, time=time.ctime(time.time())))
        # THE STUFF
        print_time(self.name, self.counter, self.delay)
        # THE STUFF has ended...
        print("Exiting {name} {time}".format(name=self.name, time=time.ctime(time.time())))


















thread1 = JBGWUThread(1, "JBGWUThread1", counter=3, delay=4)
thread2 = JBGWUThread(2, "JBGWUThread2", counter=5, delay=2)




thread1.start()
thread2.start()
print("Exiting Main {time}".format(time=time.ctime(time.time())))

