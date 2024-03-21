import sys



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    
    def insert(self, val):
        self.root = self.insertH(self.root, val)
    
    
    def remove(self, val):
        self.root = self.removeH(self.root, val)

    def insertH(self, root, val):
        if not root:
            return Node(val)
        elif val < root.val:
            root.left = self.insertH(root.left, val)
        else:
            root.right = self.insertH(root.right, val)
        
       
        root.height = 1 + max(self._height(root.left), self._height(root.right))

        balance = self._get_balance(root)
        
     
        if balance > 1 and val < root.left.val:
            return self._right_rotate(root)

        if balance < -1 and val > root.right.val:
            return self._left_rotate(root)

        if balance > 1 and val > root.left.val:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1 and val < root.right.val:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root
    
    
    def removeH(self, node, key):
        if node is None:
            return node
        elif key < node.val:
            node.left = self.removeH(node.left, key)
        elif key > node.val:
            node.right = self.removeH(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.get_min_value_node(node.right)
            node.val = temp.val
            node.right = self.removeH(node.right, temp.val)
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))
            balance = self._get_balance(node)
            if balance > 1 and self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            if balance < -1 and self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            if balance > 1 and self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
            if balance < -1 and self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        return node
     
    
    def _left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    
    def _height(self, root):
        if not root:
            return 0

        return root.height

    
    def _get_balance(self, root):
        if not root:
            return 0
        return self._height(root.left) - self._height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def preorder(self):
        self.preorderH(self.root)

    def preorderH(self, root):
        if root:
            print(str(root.val) + " ", end='')
            self.preorderH(root.left)
            self.preorderH(root.right)




    def printTree(self):
        self.printTreeH(self.root)

    def printTreeH(self, node, prefix="", is_left=True):
        if node is None:
            return

        
        print(f"{prefix}{'L' if is_left else 'R'}─({self._get_balance(node)}){node.val}")
        
        
        if node.left is not None:
            self.printTreeH(node.left, prefix + ("   | " if is_left else "   | "), True)

        
        if node.right is not None:
            self.printTreeH(node.right, prefix + ("   | " if is_left else "   | "), False)



    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, current_node, value):
        if current_node is None:
            return False
        elif current_node.val == value:
            return True
        elif value < current_node.val:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)



    

avl=AVLTree()

avl.insert(30)
avl.insert(50)
avl.insert(60)
avl.insert(80)
avl.insert(40)
avl.insert(70)
avl.insert(90)
avl.insert(10)
avl.insert(130)
avl.printTree()
print()
print("Preorder traversal:")
avl.preorder()
print()
print(avl.search(20))
