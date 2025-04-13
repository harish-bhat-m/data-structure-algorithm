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


    def set_data(self, element=None):
        """
        Sets the value of the node.
        :param: 
            element: value of the node.
        :returns: None
        :rtype: None
        :exception: If the element is none, the exception is raised.        
        """
        try:
            assert (element is not None)
            self.element = element
        except AssertionError as error:
            print("Error Case: Element cannot be empty.")

    def get_data(self):
        """
        Returns the value of the node
        :param: None
        :retunr : None
        :rtype: None
        :exception: None.
        """
        return self.element
    
    def set_next(self, next_node):
        """
        Set the pointers to the next node. Links current node with next node.
        :param: 
            next_node: pointer to the next node.
        :returns: None
        :rtype: None
        :exception: None.
        """
        self.next_node = next_node

    def get_next(self):
        """
        Returns the pointers to the next node.
        :param: None.
        "returns: None.
        :rtype: None.
        :exception: None.
        """
        return self.next_node   