# -*- coding: utf-8 -*-
#!\usr\bin\python

# import threading
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         super().__init__(self, name="threddy" + num)
#         self.num = num
#     def run(self):
#         print ("Thread ", self.num),
# thread1 = MyThread("1")
# thread2 = MyThread("2")
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"
def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread
        time.sleep(.9)                                     # ...Wait 0.9 seconds before starting another
if __name__ == '__main__':main()