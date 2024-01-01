class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self, indent=''):
        # Print the right subtree (if any), first recursively with increased indentation
        if self.right:
            self.right.print_tree(indent + '   ')
        # Print the root value
        print(indent + str(self.data))
        # Then print the left subtree (if any), also recursively with increased indentation
        if self.left:
            self.left.print_tree(indent + '   ')


if __name__ == "__main__":
    # Use the insert method to add nodes
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)

    root.print_tree()
