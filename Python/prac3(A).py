#Prac.3 write a program to demostrate concept of threading and multitasking in python
#A.Program to demostrate the concept of threading
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting",name)
    time.sleep(2)
    logging.info("Thread %s:finishing",name)


if  __name__ == "__main__":
    format ="%(asctime)s:%(message)s"
    logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main   : before creating thread")
    x=threading.Thread(target=thread_function,args=(1,))
    x.start()
    logging.info("Main   :wait for thread to finish")
    x.join()
    logging.info("Main   :all done")
