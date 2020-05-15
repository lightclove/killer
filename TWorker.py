# -*- coding: utf-8 -*-
#!\usr\bin\python

#! Python - запуск и остановка нескольких потоков
# У меня есть три функции: functionA, functionB и functionC.
# Я хочу, чтобы functionA и functionB запускались одновременно, и когда условие в функции B становится истинным,
# я хочу, чтобы функция A остановилась, functionC для запуска, а затем functionA,
# чтобы начать работать снова, наряду с функцией B.

import threading

events = threading.Event()


def worker1(events, sendFlag):
    print("Worker1")
    a, b, c = events
    while True:
        a.wait()  # sleep here if 'a' event is set, otherwise continue
        # do work here
        if sendFlag == True:
            c.clear()  # put c to sleep
            b.set()  # wake up, b


def worker2(events, sendFlag):
    print("Worker2")
    a, b, c = events
    while True:
        b.wait()
        # do work
        if sendFlag == True:
            a.clear()  # put a to sleep
            c.set()  # wake up, c


def worker3(events, sendFlag):
    print("Worker3")
    a, b, c = events
    while True:
        c.wait()
        # do work
        if sendFlag == True:
            b.clear()  # put b to sleep
            a.set()  # wake up, c

# Если флаг был задан, метод wait не будет делать ничего.
# Если флаг был убран, wait будет блокировать, пока его снова не установят.
# Любое количество потоков может дожидаться одного и того же объекта event.


if __name__ == '__main__':

    events = [threading.Event() for _ in range(3)]
    events[0].set()
    events[1].set()
    # events[2] starts un-set, i.e. worker3 sleeps at start
    threads = []
    sendFlag = True
    threads.append(threading.KillableThread(target=worker1, args=(events, sendFlag)))
    threads.append(threading.KillableThread(target=worker2, args=(events, sendFlag)))
    threads.append(threading.KillableThread(target=worker3, args=(events, sendFlag)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()
