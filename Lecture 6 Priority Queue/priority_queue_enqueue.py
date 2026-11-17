class Node:
    def __init__(self,value,pr):
        self.data = value
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self,new_node):
        if self.front == None:
            self.front = new_node
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return
        else:
            temp = self.front
            while temp.next:
                if new_node.priority <= temp.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next
            prev.next = new_node
            new_node.next = temp

    def display(self):
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
    
pq = PriorityQueue()
pq.enqueue(Node(200,2))
pq.enqueue(Node(300,5))
pq.enqueue(Node(777,7))
pq.enqueue(Node(900,3))
pq.enqueue(Node(1000,9))
pq.display()
            
