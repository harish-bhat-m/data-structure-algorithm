class ListNode(object):
    """
    Implementation of node which is used to implement the linked list.
    It contains the value of the node and the pointer to the next node.
    Method to iterate the linked list
    """
    def __init__(self, value=0, next_node=None):
        """
        Initializing the nodes attributes.
        :param:
            value: value of the node.
            next_node: pointer to the next node.
        :returns: None.
        :rtype: None.
        :exception: None
        """
        self.value = value
        self.next_node = next_node

    def iterate(self):
        """
        Method to iterate the linked list
        :param: None
        :returns: None
        :rtype: None
        :exception: None    
        """
        node = self
        while node:
            print(node.value, end=" | ")
            node = node.next_node
        print()

root1 = ListNode(2, ListNode(4, ListNode(3, ListNode(5, ListNode(6, ListNode(4))))))
root2 = ListNode(5, ListNode(6, ListNode(4)))
root1.iterate()
root2.iterate()
