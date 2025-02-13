# Simple stack implementation in python

class Stack(object):
    '''
    Simple stack implementation.
    Basic Operation:
        Push: Add an element to the top of a stack
        Pop: Remove an element from the top of a stack
        IsEmpty: Check if the stack is empty
        IsFull: Check if the stack is full
        Peek: Get the value of the top element without removing it
    '''

    def __init__(self, size_of_stack):
        '''
        Initialization of stack
        :param size_of_stack: The size of the stack
        :type size_of_stack: int
        '''
        self.size_of_stack = size_of_stack
        self.stack = []

    def isFull(self):
        '''
        Check if the stack is full
        :return: True if the stack is full otherwise False
        :rtype: bool'''
        if len(self.stack) == self.size_of_stack:
            return True
        else:
            return False

    def isEmpty(self):
        '''Check if the stack is empty or not
        : return True if the stack is empty else False
        : rtype: bool'''
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def push(self, element):
        '''
        Add an element to the top of the stack.
        
        :param element: The element to be added
        :type element: object
        :raises IndexError: If the stack is full
        '''
        if self.isFull():
            raise IndexError("Stack is full")
        # Add the element to the stack
        self.stack.append(element)
        print("Added {} to the stack".format(element))
        
    def pop(self):
        '''
        Removes an top element from the stack
        : returns: top most element from the stack
        : rtyep: object
        : raises IndexError: if the stack is empty
        '''
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            print("Removed {} from the stack".format(self.stack[-1]))
            return self.stack.pop()
        
    def peek(self):
        '''
        Get the top element of the stack without removing it
        : returns: top most element from the stack
        : rtype: object
        : raises IndexError: if the stack is empty
        '''
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            return self.stack[-1]
        
    def display(self):
        '''
        Dispaly all the elements from the stack
        : return : list of objects
        : rtype: list
        : raises IndexError : if the stack is empty
        '''
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            print("\n", end = "|")
            for element in self.stack:
                print("{}".format(element), end="|")
            print()

# Initializing the stack
if __name__ == "__main__":                
    stk = Stack(5)
    stk.push("A")
    stk.push("B")
    stk.push("C")
    stk.display()
    stk.pop()
    stk.pop()
    stk.pop()
    #stk.display()

    