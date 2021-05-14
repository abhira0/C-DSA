from stack_queue import Queue


class BTNode:
    def __init__(self, key, left_node=None, right_node=None, parent=None) -> None:
        self.key = key
        self.left = left_node
        self.right = right_node
        self.parent = parent


class BinaryTree:
    def __init__(self, root: BTNode = None) -> None:
        self.root = root

    def inOrderTraversalhelper(self, node: BTNode):
        if node == None:
            return
        self.inOrderTraversalhelper(node.left)
        print(node.key, end=", ")
        self.inOrderTraversalhelper(node.right)

    def inOrderTraversal(self):
        if self.root:
            self.inOrderTraversalhelper(self.root)
        else:
            print("EMPTY TREE")

    def preOrderTraversalhelper(self, node: BTNode):
        if node == None:
            return
        print(node.key, end=", ")
        self.inOrderTraversalhelper(node.left)
        self.inOrderTraversalhelper(node.right)

    def preOrderTraversal(self):
        if self.root:
            self.inOrderTraversalhelper(self.root)
        else:
            print("EMPTY TREE")

    def postOrderTraversalhelper(self, node: BTNode):
        if node == None:
            return
        self.inOrderTraversalhelper(node.left)
        self.inOrderTraversalhelper(node.right)
        print(node.key, end=", ")

    def postOrderTraversal(self):
        if self.root:
            self.inOrderTraversalhelper(self.root)
        else:
            print("EMPTY TREE")

    def breadthFirstSearch(self):
        q = Queue()
        q.enqueue(self.root)
        while not q.isEmpty():
            tmp = q.dequeue()
            print(tmp.key)
            if tmp.left:
                q.enqueue(tmp.left)
            if tmp.right:
                q.enqueue(tmp.right)
