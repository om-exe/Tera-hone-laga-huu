from multiprocessing import Process,Queue
import time

def producer(queue):
    for i in range (5):
        item = f"Item {i+1}"
        queue.put(item)
        print(f"Producer produced {item}")
        time.sleep(1)

def consumer(queue):
    while True:
        item=queue.get()
        if item is None:
            break
        print(f"Consumer consumed {item}")
        time.sleep(2)
if __name__=='__main__':
    queue=Queue()
    producer_process=Process(target=producer,args=(queue,))
    consumer_process=Process(target=consumer,args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    queue.put(None)
    consumer_process.join()

# Output
# Producer produced Item 1
# Consumer consumed Item 1
# Producer produced Item 2
# Consumer consumed Item 2
# Producer produced Item 3
# Producer produced Item 4
# Consumer consumed Item 3
# Producer produced Item 5
# Consumer consumed Item 4
# Consumer consumed Item 5