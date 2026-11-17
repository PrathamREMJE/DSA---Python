# Node class for linked list based Queue
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

# Queue class implementing Enqueue, Dequeue, Display, Reverse, Merge, and Compare
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None   

    def is_empty(self):
        return self.front is None

    # 1. Enqueue an element into the queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued {data}")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data}")

    # 2. Dequeue an element from the queue
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

    # 3. Display queue elements
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

    # 4. Reverse the queue using a stack
    def reverse_queue(self):
        stack = []
        temp = self.front
        while temp:
            stack.append(temp.data)
            temp = temp.next
        temp = self.front
        while temp:
            temp.data = stack.pop()
            temp = temp.next
        print("Queue reversed")

    # 5. Merge two queues into one
    def merge_queues(q1, q2):
        merged_q = Queue()
        temp = q1.front
        while temp:
            merged_q.enqueue(temp.data)
            temp = temp.next
        temp = q2.front
        while temp:
            merged_q.enqueue(temp.data)
            temp = temp.next
        return merged_q

    # 6. Check if two queues are identical
    def are_identical(q1, q2):
        t1 = q1.front
        t2 = q2.front
        while t1 and t2:
            if t1.data != t2.data:
                return False
            t1 = t1.next
            t2 = t2.next
        return t1 is None and t2 is None

# Example usage for Q.2
if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.display()
    q1.dequeue()
    q1.display()
    print("\nReverse Queue using Stack")
    q1.reverse_queue()
    q1.display()
    print("\nMerge Two Queues")
    q2 = Queue()
    q2.enqueue(40)
    q2.enqueue(50)
    print("Queue 1:")
    q1.display()
    print("Queue 2:")
    q2.display()
    merged_queue = Queue.merge_queues(q1, q2)
    print("Merged Queue:")
    merged_queue.display()

    print("\nCheck if Two Queues are Identical")
    q3 = Queue()
    q3.enqueue(20)
    q3.enqueue(30)
    print("Queue 1 and Queue 3 identical?", Queue.are_identical(q1, q3))