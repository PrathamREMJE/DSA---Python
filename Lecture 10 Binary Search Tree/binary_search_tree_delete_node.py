class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:  #BST is empty
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def min_value(self, temp):
        if temp is None:
            return None
        else:
            while temp.left is not None:
                temp = temp.left
            return temp.data

    def max_value(self, temp):
            if temp is None:
                return None
            else:
                while temp.right is not None:
                    temp = temp.right
                return temp.data

    def del_node(self, rt, val):
        if rt is None:
            return rt
        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            if rt.left is None:
                return rt.right
            elif rt.right is None:
                return rt.left
            successor = self.get_successor(rt.right)
            rt.data = successor
            rt.right = self.del_node(rt.right, successor)
        return rt

    def get_successor(self, rt):
        if rt is None:
            return None
        else:
            while rt.left is not None:
                rt = rt.left
            return rt.data


b1 = BST()
b1.insert(Node(200))
b1.insert(Node(20))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
b1.del_node(b1.root, 20)
b1.inorder(b1.root)