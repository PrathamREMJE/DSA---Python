# Node class for linked list based Stack
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

# Stack class implementing Push, Pop, Display, Reverse String, and Reverse Stack
class Stack:
    def __init__(self):
        self.top = None  

    def is_empty(self):
        return self.top is None

    # 1. Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Data Pushed")

    # 2. Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        pop_data = self.top.data
        self.top = self.top.next
        print(f"Pop - {pop_data}")
        return pop_data

    # 3. Display operation
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        temp = self.top
        print("Stack Data: ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 4. Reverse String using Stack
    def reverse_string(text):
        s = Stack()
        for char in text:
            s.push(char)
        reversed = ""
        while not s.is_empty():
            reversed += s.pop()
        return reversed

    # 5. Reverse Stack using another Stack
    def reverse_stack(self):
        temp_stack1 = Stack()
        temp_stack2 = Stack()
        while not self.is_empty():
            temp_stack1.push(self.pop())

        while not temp_stack1.is_empty():
            temp_stack2.push(temp_stack1.pop())

        while not temp_stack2.is_empty():
            self.push(temp_stack2.pop())

if __name__ == "__main__":
    stk = Stack()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    stk.display()
    stk.pop()
    stk.display()

    print("\n--- Reverse String using Stack ---")
    str = "Hello World"
    rev_str = Stack.reverse_string(str)
    print(f"Original String: {str} and Reversed String: {rev_str}")

    print("\n--- Reverse Stack using another Stack ---")
    print("Before reversal:")
    stk.display()
    stk.reverse_stack()
    print("After reversal:")
    stk.display()