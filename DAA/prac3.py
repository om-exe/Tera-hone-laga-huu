class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Stack:
    def __init__(self) -> None:
        self.head = None
    def pop(self):
        if self.head is None:
            return None
        else:
            popped  = self.head.data
            self.head = self.head.next
            return popped
a_stack = Stack()
while True:
    print('push <value> ')
    print('pop')
    print('quit')
    do = input("What would u like to do ").split()
    operation  =do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation=='pop':
        popped = a_stack.pop()
        if popped is None:
            print("popped value",int(popped))
        else:
            print("popped value ",int(popped))
    elif operation =='quit':
        break
