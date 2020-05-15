# -*- coding: utf-8 -*-
#!\usr\bin\python
import threading

class ThreadedFunction():
    def threaded(fn, callback_func, isStop):
        """To use as decorator to make a function call threaded.
        It will call the callback_func when the function returns.
        Needs import
        from threading import Thread"""
        def wrapper(*args, **kwargs):
            def do_callback():
                callback_func(fn(args, kwargs))
            thread = threading.KillableThread(target=do_callback)
            thread.start()
            if isStop:
                print("Exit from thread")
                thread._stop()
            return thread
        return wrapper

    #@threaded
    def wannaThread(self, isStop):
        while isStop != True:
             print("I want to run this in separate thread!")

########################################################################################################################

def threaded(fn, callback_func):
    """To use as decorator to make a function call threaded.
    It will call the callback_func when the function returns.
    Needs import
    from threading import Thread"""
    def wrapper(*args, **kwargs):
        def do_callback():
            callback_func(fn(args, kwargs))
        thread = threading.KillableThread(target=do_callback)
        thread.start()
        return thread
    return wrapper

import queue
result = queue.Queue

def thread(resultQueue=None):
    def wrapper(function):
        def pw(*args, **kwargs):
            def process(*args, **kwargs):
                # print(args, kwargs)
                ret = function(*args, **kwargs)
                if resultQueue:
                    resultQueue.put(ret)
                # return resultQueue
            thread = threading.KillableThread(target=process, args=args, kwargs=kwargs)
            thread.setDaemon(True)
            thread.start()
            return process
        return pw
    return wrapper

########################################################################################################################

