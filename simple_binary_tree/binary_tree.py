""" Binary tree implementation in Python"""
class BinaryTree():
    """ Binaary tree implemnetation"""
    def __init__(self, root):
        self.key = root
        self.right_child = None
        self.left_child = None

    def set_left_child(self, new_node):
        """ sets the new node to the left child"""
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            temp_node = BinaryTree(new_node)
            temp_node.left_child = self.left_child
            self.left_child = temp_node

    def set_right_child(self, new_node):
        """ sets the new node to right child"""
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            temp_node = BinaryTree(new_node)
            temp_node.right_child = self.right_child
            self.right_child = temp_node

    def set_root_node(self, obj):
        """ sets the root node"""
        self.key = obj


    def get_left_child(self):
        """ Returns the left child of the node"""
        return self.left_child

    def get_righ_child(self):
        """ Returns the right child of the node"""
        return self.right_child

    def get_root_node(self):
        """ Returns  root value of the node"""
        return self.key

if __name__== "__main__":
    binary_tree = BinaryTree("A")
    binary_tree.set_left_child("B")
    binary_tree.set_right_child("C")

    print(binary_tree.get_left_child().get_root_node())
