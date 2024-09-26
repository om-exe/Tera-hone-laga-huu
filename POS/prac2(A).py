import time
def task (name,delay):
    print(f"Task '{name}' completed")

def main():
    print("Main program started")

    task("Task 1 ",2)
    task("Task 2 ",1)
    task("Task 3 ",3)

    print("Main program completed")
if __name__=="__main__":
    main()

# Output
# Main program started
# Task 'Task 1 ' completed
# Task 'Task 2 ' completed
# Task 'Task 3 ' completed
# Main program completed