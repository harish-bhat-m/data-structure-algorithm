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
        if isinstance(value, int):
            print("Its Int")
            self.value = value
            self.next_node = next_node
        elif isinstance(value, list):
            root = self
            for val in value:
                self.value = val
                self.next_node = self
                self = self.next_node
            self= root
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

class Solution:
    """
    Class to implement the solution to add the two linked list
    :param: None
    :returns: None
    :rtype: None
    :exception: None
    """
    def add_two_linked_list(self, linked_list_1: ListNode, linked_list_2:ListNode) -> ListNode:
        """
        Method to add the two linked list
        :param: 
            linked_list_1: linked list 1
            linked_list_2: linked list 2
        :returns: Sum of the linked list
        :rtype: ListNode
        :exception: None    
        """
        result = ListNode()
        ptr = result

        carry = 0
        while linked_list_1 is not None or linked_list_2 is not None:
            sum = 0 + carry

            if linked_list_1 is not None:
                sum += linked_list_1.value
                linked_list_1 = linked_list_1.next_node

            if linked_list_2 is not None:
                sum += linked_list_2.value
                linked_list_2 = linked_list_2.next_node

            carry = sum // 10
            sum = sum % 10

            ptr.next_node = ListNode(sum)
            ptr = ptr.next_node

            if carry == 1:
                ptr.next_node = ListNode(1)
            
        #return result.next_node              
        return result.next_node
        
root_1 = ListNode([1,3,4])
root_2 = ListNode(2, ListNode(5, ListNode(6)))
root_1.iterate()
root_2.iterate()
"""root1 = ListNode(9,
                 ListNode(9,
                          ListNode(9,
                                   ListNode(9,
                                            ListNode(9,
                                                     ListNode(9,
                                                              ListNode(9)))))))

root2 = ListNode(9,
                 ListNode(9,
                          ListNode(9,
                                   ListNode(9))))


sol = Solution()
sum = sol.add_two_linked_list(root1, root2)
root1.iterate()
root2.iterate()
sum.iterate()"""
