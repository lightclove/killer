# -*- coding: utf-8 -*-
#!\usr\bin\python
#! Custom thread class which were created if you want to stop this thread from another part of the progrgramm i. e.
# from another func
# The thread itself has to check
# regularly for the stopped() condition."""
# Если флаг был задан, метод wait не будет делать ничего.
# Если флаг был убран, wait будет блокировать, пока его снова не установят.
# Любое количество потоков может дожидаться одного и того же объекта event.

import threading
from threading import Thread


class CustomThread(threading.Thread):
    def init(self, target, args):
        super(CustomThread, self).__init__()
        self._stop_event = threading.Event()


    def stopped(self):
        return self._stop_event.is_set()

    def stop(self):
        self._stop_event.set()


    def threaded_function(self, threaded_function, isStop):
        def wrapper(*args, **kwargs):
            custom_thread = threading.KillableThread(target=threaded_function, args=args, kwargs=kwargs)
            custom_thread.start()
            if(isStop):
                return
        return wrapper


