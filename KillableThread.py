# -*- coding: utf-8 -*-
#!\usr\bin\python
import threading

class KillableThread(threading.Thread):
    def __init__(self, sleep_interval=1):
        super().__init__()
        self._kill = threading.Event()
        self._interval = sleep_interval

    def run(self):
        while True:
            print("Do Something")
            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill.wait(self._interval)
            if is_killed:
                break

        print("Killing Thread")

    def kill(self):
        self._kill.set()

t = KillableThread(sleep_interval=5)
t.start()
# Every 5 seconds it prints:
#: Do Something
t.kill()
#: Killing Thread