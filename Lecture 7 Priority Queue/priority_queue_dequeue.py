class Node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

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
        if self.front:
            temp = self.front
            print("Node Deleted:", temp.data)
            self.front = self.front.next
        else:
            print("Queue is empty")

    def display(self):
        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


pq = PriorityQueue()

pq.enqueue(Node(200, 2))
pq.enqueue(Node(300, 5))
pq.enqueue(Node(777, 7))
pq.enqueue(Node(900, 3))
pq.enqueue(Node(1000, 9))
pq.dequeue()


pq.display()
