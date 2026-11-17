class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print("Inserted:", value)

    def display(self):
        if not self.stack:
            print("Stack is empty")
            return
        for value in reversed(self.stack):
            print(value, end=" ")
        print("None")

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None   

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued {data}")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {temp.data}")
        return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        print("Queue Data: ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

def reverse_queue(queue):
    s1 = Stack()
    while not queue.is_empty():
        s1.push(queue.dequeue())
    s1.display()

def reverse_stack(stack):
    queue = Queue()
    while stack.stack:
        queue.enqueue(stack.stack.pop())
    queue.display()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
reverse_queue(queue)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
reverse_stack(stack)



