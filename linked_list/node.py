class Node(object):
    """Implementation of node which is used to implement the linked list.
        Attrubutes: 
            :value: value of the node.
            :next_node: pointer to the next node.
        Methods:
            __inti__: constructor which set the attribute.
            get_value: returns the value of the node.
            set_value: sets the value of the node.
            get_next: returns the pointer to the next node.
            set_next: sets the pointer to the next node.
    """
    def __init__(self, element=None):
        """
        Initializing the nodes attributes.
        :param:
            element: value of the node.
        :returns: None.
        :rtype: None.
        :exception: If the element is none, the exception is raised.

        """
        try:
            assert (element is not None)
            self.element = element
            self.next_node = None
        except AssertionError as error:
            print("Error Case: Element cannot be empty.")