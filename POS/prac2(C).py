import threading 

class FibonaaciThread(threading.Thread):
    def __init__(self,n):
        threading.Thread.__init__(self)
        self.n=n

    def run(self):
        fib_sequene=self.generate_fibonacci(self.n)
        print(f"Fibonacci sequence for {self.n}:{fib_sequene}\n")
    def generate_fibonacci(self,n):
        fib_sequene=[0,1]
        for i in range (2,n):
            fib_sequene.append(fib_sequene[i-1]+fib_sequene[i-2])
        return fib_sequene

if __name__=="__main__":
    n1=10
    n2=15

    thread1=FibonaaciThread(n1)
    thread2=FibonaaciThread(n2)