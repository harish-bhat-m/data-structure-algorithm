from node import Node

class LinkedList(object):
    """
    Implementation of simple linked list
    Attributes:
        head: head of the linked list.
        count: Contains the count of the nodes in the linked list.
    Methods:
        __init__: Initializes the linked list attributes.
        insert: Inserts the node in the linked list.
        remove: removes the node from the linked list.
        traverse: traverses and prints the linked list elements, 
        find: finds and returns the node from the linked list.
        get_count: returns the count of the nodes in the linked list.
        is_empty: checks the linked list is empty or not.
    """
    def __init__(self, head=None):
        """
            Initializes the linked list attributes.
            :param:
                head: head of the linked list. Default will be None.
            :returns: None.
            :rtype: None.
            :exception: None.
        """
        self.head = head
        self.count = 0

    def insert(self, element = None):
        """
        Inserts the node in the linked list.
        :param: 
            element: value of the node.
        :returns: None
        :rtype: None
        :exception: If the element is None, the exception is raised.
        """
        try:
            assert (element is not None)
            new_node = Node(element)
            new_node.set_next(self.head)
            self.head = new_node
            self.count += 1
        except AssertionError as error:
            print("Error Case: Element cannot be empty.")

    def traverse(self):
        """
            Traverses the linked list and prints the nodes.
            :param: None.
            :returns: None.
            :rtype: None.
            :exception: None.
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data())
            current_node = current_node.get_next()

    def find(self, element = None):
        """
            Finds and prints the node data if found in the linked list
            :param:
                element: value of the node.
            :returns: None.
            :rtype: None.
            :exception: None.
        """
        try:
            assert (element is not None)
            current_node = self.head
            search_flag = False
            while current_node is not None:
                if current_node.get_data() == element:
                    search_flag = True
                    break
                current_node = current_node.get_next()

            if search_flag:
                print("Element '{}' found in the linked list.".format(element)) 
            else:
                print("Element '{}' not found in the linked list.".format(element))
        except AssertionError as error:
            print("Error Case: Element cannot be empty in 'find' method")
            
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert("A")
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)
    ll.traverse()
    ll.find()

