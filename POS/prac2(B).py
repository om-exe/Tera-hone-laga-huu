import time
import threading
def task (name,delay):
    print(f"Task '{name}' started")
    time.sleep(delay)
    print(f"Task '{name}' completed")


def main():
    print("Main program started")

    t1=threading.Thread(target=task,args=("Task 1 ",2))
    t2=threading.Thread(target=task,args=("Task 2 ",1))
    t3=threading.Thread(target=task,args=("Task 3 ",3))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("Main program completed")
    
if __name__=="__main__":
    main()

# Output
# Main program started
# Task 'Task 1 ' started
# Task 'Task 2 ' started
# Task 'Task 3 ' started
# Task 'Task 2 ' completed
# Task 'Task 1 ' completed
# Task 'Task 3 ' completed
# Main program completed