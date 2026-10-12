# Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None  

    def push(self, new_node: Node):
        """Appends a node to the end of the list"""
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        """Inserts a node at a specific position"""
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while temp and p < pos - 1:
                temp = temp.next
                p += 1
            if temp:
                new_node.next = temp.next
                temp.next = new_node

    def delete(self, value):
        """Deletes the first occurrence of a specific value"""
        temp = self.head
        if not temp:
            print("List is empty")
            return
        
        if temp.data == value:
            self.head = self.head.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value is not present in the list")
            return

        prev.next = temp.next

    def reverse(self):
        """Reverses the linked list"""
        curr = self.head
        prev = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        self.head = prev

    def findmid_del(self):
        """Finds and deletes the middle node"""
        if not self.head or not self.head.next:
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        print("Middle Node:", slow.data)
        if prev:
            prev.next = slow.next

    def del_firstlast(self):
        """Deletes both the first and last nodes"""
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return

        # Delete first node
        self.head = self.head.next

        # Delete last node
        temp = self.head
        prev = None
        while temp.next != None:
            prev = temp
            temp = temp.next
        if prev:
            prev.next = None

    def print_list(self):
        """Traverses and prints the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next

# --- Driver Code ---
if __name__ == "__main__":
    n1 = Node(0)
    n2 = Node(12)
    n3 = Node(90)
    n4 = Node(45)

    list1 = Linked_list()
    list1.push(n1)
    list1.push(n2)
    list1.push(n3)
    list1.push(n4)

    print("Initial List:")
    list1.print_list()

    print("\nAfter Reversing:")
    list1.reverse()
    list1.print_list()