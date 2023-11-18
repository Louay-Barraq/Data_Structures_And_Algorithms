class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data < self.data:
            if not self.left:
                self.left = BinarySearchTreeNode(data)
            else:
                self.left.add_child(data)

        elif data > self.data:
            if not self.right:
                self.right = BinarySearchTreeNode(data)
            else:
                self.right.add_child(data)

        else:
            print(f"Can't add {data} because it already exists !")

    def add_children(self, values):
        for value in values:
            self.add_child(value)

    def search(self, data):
        if self.data == data:
            return True

        elif self.data > data:
            if self.left:
                self.left.search(data)
            else:
                return False

        else:
            if self.right:
                self.right.search(data)
            else:
                return False

    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()

    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    def in_order_traversal(self):
        all_elements = []

        # Append left child node
        if self.left:
            all_elements += self.left.in_order_traversal()

        # Append current node
        all_elements.append(self.data)

        # Append right child node
        if self.right:
            all_elements += self.right.in_order_traversal()

        return all_elements

    def delete(self, data):
        # Locate data to delete
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)

        else:
            # Node doesn't have children |=> Delete node directly
            if not self.left and not self.right:
                return None
            # Node has only a left child
            elif not self.right:
                return self.left
            # Node has only a right child
            elif not self.left:
                return self.right
            # Node has 2 children
            else:
                # Look for the minimum in the right subtree
                right_subtree_min = self.right.minimum()
                # Replace current node with that minimum
                self.data = right_subtree_min
                # remove the original minimum node
                self.right = self.right.delete(right_subtree_min)

        return self

