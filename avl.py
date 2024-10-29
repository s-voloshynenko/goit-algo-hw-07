class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                # L - L
                return self.right_rotate(root)
            else:
                # L - R
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                # R - R
                return self.left_rotate(root)
            else:
                # R - L
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # most right
    def max(self, root):
        if root is None:
            return None
        elif root.right is None:
            return root.key

        return self.max(root.right)

    # most left
    def min(self, root):
        if root is None:
            return None
        elif root.left is None:
            return root.key

        return self.min(root.left)

    def sum(self, root):
        if root is None:
            return 0

        return root.key + self.sum(root.left) + self.sum(root.right)
