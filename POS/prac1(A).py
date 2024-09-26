import threading
import queue
sq = queue.Queue()
class Producer(threading.Thread):
    def run(self):
        for i in range(5):
            item = f" Item { i } "
            sq.put(item)
            print(f" Produced { item } ")
        sq.put(None)
class Consumer (threading.Thread):
    def run(self):
        while True:
            item = sq.get()
            if item is None:
                break
            print(f" Consumed { item } ")
p = Producer()
c = Consumer()
p.start()
c.start()
p.join()
c.join()


# Output
#  Produced  Item 0  
#  Consumed  Item 0  
#  Produced  Item 1  
#  Produced  Item 2  
#  Produced  Item 3  
#  Consumed  Item 1  
#  Produced  Item 4  
#  Consumed  Item 2  
#  Consumed  Item 3  
#  Consumed  Item 4 
