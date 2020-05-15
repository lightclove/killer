# -*- coding: utf-8 -*-
#!\usr\bin\python

"""Thread class with a stop() method. The thread itself has to check
regularly for the stopped() condition."""

import threading
import time


class StoppableThread(threading.Thread):
    def __init__(self, target, args):
        super().__init__(self)
        # super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def __init__(self, isStop):
        self._stop_event = threading.Event()
        if self.stopped() != True : self.stop()
        self.stop()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


