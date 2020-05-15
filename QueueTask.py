# -*- coding: utf-8 -*-
#!\usr\bin\python

import os
import threading

from queue import Queue


class QueueTask(threading.Thread):
    """Потоковый загрузчик файлов"""

    def __init__(self, queue):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self, isStop):
        """Запуск потока"""
        while True:

            print("do something Logic")
            #old
            # # Получаем url из очереди
            # url = self.queue.get()
            #
            # # Скачиваем файл
            # self.download_file(url)
            #
            # # Отправляем сигнал о том, что задача завершена
            # self.queue.task_done()

            if(isStop == True):
                self.stop()

    def stop(self):
            """Stop потока"""
            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()



#
    queue = Queue()

    # Запускаем потом и очередь
    # for i in range(5):
    #     t = QueueTask(queue)
    #     t.setDaemon(True)
    #     t.start()

    # Даем очереди нужные нам ссылки для скачивания
    #for url in urls:
    #    queue.put(url)

    # Ждем завершения работы очереди
    # queue.join()


if __name__ == "__main__":
    print("starting")