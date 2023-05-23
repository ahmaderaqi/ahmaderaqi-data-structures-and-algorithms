class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self):
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node is not None:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)

    def post_order_traversal(self):
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node, result):
        if node is not None:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)





class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add_recursive(current.right, value)

    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._contains_recursive(current.left, value)
        else:
            return self._contains_recursive(current.right, value)



