#Program to demostrate the concept of multitasking
import _thread as thread,time
def counter(myID,count):
    for i in range (count):
        time.sleep(1)
        mutex.acquire()
        print("Thread [%s]=>%s"%(myID,i))
        mutex.release()

mutex=thread.allocate_lock()
for i in range(3):
    thread.start_new_thread(counter,(i,3))
    time.sleep(6)
print('Main thread exit')
