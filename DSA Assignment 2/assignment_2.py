# Practical Assignment 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    # 1. Create Linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("Node created")

    # 2. Traverse and print node values
    def traverse(self):
        if self.head is None:
            print("Linked list empty")
            return
        temp = self.head
        print("Linked list:", end=" ")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert node at a specific position
    def insert(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            print("Node inserted")
            return
        temp = self.head
        current_pos = 1
        while temp is not None and current_pos < pos - 1:
            temp = temp.next
            current_pos += 1
        if temp is None:
            print("Invalid position")
            return
        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted")

    # 4. Delete alternate nodes
    def delete_alternate(self):
        if self.head is None:
            print("Linked list empty")
            return
        temp = self.head
        while temp is not None and temp.next is not None:
            temp.next = temp.next.next
            temp = temp.next
        print("Alternate nodes deleted")

# Main program
linked_list = Linkedlist()
while True:
    print("\n- Singly Linear Linked list -")
    print("1. Create Linked list")
    print("2. Traverse and Print")
    print("3. Insert Node at Specific position")
    print("4. Delete Alternate Nodes")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        data = int(input("Enter node value to append: "))
        linked_list.append(data)
    elif choice == "2":
        linked_list.traverse()
    elif choice == "3":
        data = int(input("Enter value to insert: "))
        pos = int(input("Enter position (starting from 1): "))
        linked_list.insert(data, pos)
    elif choice == "4":
        linked_list.delete_alternate()
    elif choice == "5":
        print("Program End")
        break
    else:
        print("Invalid choice")
