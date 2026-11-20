class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return
        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return
        temp = self.front
        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
            return
        temp = self.front
        print("Process Executed:", temp.pid, temp.name)
        print("-----------------------------")
        self.front = self.front.next

    def display_next(self):
        if self.front == None:
            print("Queue is empty")
            return
        print("Next Process:")
        print("Process ID:", self.front.pid)
        print("Process Name:", self.front.name)
        print("Priority:", self.front.priority)
        print("-----------------------------")

    def display_all(self):
        if self.front == None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next
        print("-----------------------------")

    def count(self):
        temp = self.front
        total = 0
        while temp:
            total += 1
            temp = temp.next
        print("Total Pending Processes:", total)

pq = PriorityQueue()
pq.enqueue(Node(101, "Backend Process", 3))
pq.enqueue(Node(102, "System Process", 1))
pq.enqueue(Node(103, "Interactive Process", 2))
pq.enqueue(Node(104, "Low level Process", 4))
pq.display_all()
pq.display_next()
pq.dequeue()
pq.display_next()
pq.display_all()
pq.count()
