# Singly Linear Linked List Program Assignment  
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create_list(self, values):
        self.head = None
        for value in values:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

        print("Linked List Created")

    # 2. Traverse and print node values
    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert node at a specific position
    def insert(self, data, position):
        if position < 1:
            print("Invalid position.")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print("Node inserted")
            return
        temp = self.head
        current_position = 1
        while temp is not None and current_position < position - 1:
            temp = temp.next
            current_position += 1
        if temp is None:
            print("Invalid position")
            return
        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted")

    # 4. Find middle node and print its value
    def find_middle(self):
        if self.head is None:
            print("Linked List is empty")
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("Middle node value:", slow.data)

    # 5. Delete node at a specific position
    def delete(self, position):
        if self.head is None:
            print("Linked List is empty")
            return
        if position < 1:
            print("Invalid position")
            return
        if position == 1:
            self.head = self.head.next
            print("Node deleted")
            return
        temp = self.head
        current_position = 1
        while temp.next is not None and current_position < position - 1:
            temp = temp.next
            current_position += 1
        if temp.next is None:
            print("Invalid position")
            return
        temp.next = temp.next.next
        print("Node deleted")

    # 6. Reverse Linked List
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        print("Linked List reversed")

    # 7. Sum of every two consecutive node values
    def consecutive_sums(self):
        if self.head is None or self.head.next is None:
            print("At least two nodes are needed")
            return
        temp = self.head
        print("Sums of consecutive node pairs:")
        while temp.next is not None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next

# Main program
linked_list = LinkedList()
while True:
    print("\n-Singly Linear Linked List-")
    print("1. Create Linked List")
    print("2. Traverse and Print")
    print("3. Insert Node")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Sum of Consecutive Nodes")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        values = list(map(int, input(
            "Enter node values separated by spaces: "
        ).split()))
        linked_list.create_list(values)
    elif choice == "2":
        linked_list.traverse()
    elif choice == "3":
        data = int(input("Enter value to insert: "))
        position = int(input("Enter position (starting from 1): "))
        linked_list.insert(data, position)
    elif choice == "4":
        linked_list.find_middle()
    elif choice == "5":
        position = int(input("Enter position to delete: "))
        linked_list.delete(position)
    elif choice == "6":
        linked_list.reverse()
    elif choice == "7":
        linked_list.consecutive_sums()
    elif choice == "8":
        print("Program terminated")
        break
    else:
        print("Invalid choice")
