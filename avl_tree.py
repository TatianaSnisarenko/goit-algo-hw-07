from queue import Queue
from avl_node import AVLNode


class AVLTree:
    def __init__(self):
        self.root = None

    def __str__(self, node=None, level=0, prefix="Root: "):
        if not node:
            node = self.root
        ret = "\t" * level + prefix + str(node) + "\n"
        if node.left:
            ret += self.__str__(node.left, level + 1, "L--- ")
        if node.right:
            ret += self.__str__(node.right, level + 1, "R--- ")
        return ret

    def sum(self):
        current = self.root
        if not current:
            return 0
        else:
            sum = 0
            queue = Queue()
            queue.put(current)
            while not queue.empty():
                current = queue.get()
                sum += current.key
                if current.left:
                    queue.put(current.left)
                if current.right:
                    queue.put(current.right)
        return sum

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def min_value_node(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def max_value_node(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def insert_node(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete_node(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node()
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root
