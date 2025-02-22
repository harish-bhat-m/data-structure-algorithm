# Implementation of simple double ended queue in python

class Dqueue(object):
    '''
    This is class for impmenting the double ended queue.
    The double ended queue which will inserts or removes the 
    elements from the queue from both the ends.

    Types of the dqueue:
        1. Input Restricted Dqueue: 
            Input is restricted to single end but deletion at both the ends.
        2. Output Restricted Dqueue:
            Output is restricted to single end but insertion at both the ends.
    
    -- Methods:
    : insert at the front of the queue.
    : insert at the back of the queue.
    : delete from the front of the queue.
    : delete from the back of the queue.
    : check empty or not.
    : check full or not.
    : dispay the queue. 
    : rear peek.
    : front peek.
    '''

    def __init__(self, size_of_queue):
        '''
        Initialization of the doube ended queue.
        :param: None
        :returns: None
        :rtype: None
        '''
        self.dqueue = []
        self.size_of_queue = size_of_queue

    def isEmpty(self):
        '''
        Check if the dqueue is empty or not.
        :param: None.
        :returns: None
        :rtype: bool.
        '''

        if len(self.dqueue) == 0:
            return True
        else:
            return False
    
    def isFull(self):
        '''
        Check if the dqueue is full or not.\
        :param: None.
        :returns: None.
        :rtype: bool
        '''
        if len(self.dqueue) == self.size_of_queue:
            return True
        else:
            return False
        
    def addRear(self, element):
        '''
        Add an element to the back of the queue.
        :param: element: the element which need to be added to the queue from rear
        :returns: None
        rtype: None
        '''
        if self.isFull():
            raise Exception("Queue is full.")
        else:
            self.dqueue.append(element)

    
    def addFront(self, element):
        '''
        Add an element to the front of the queue.
        :param: element: the element which need to be added to the queue from front.
        :returns: None
        :rtype: None
        '''
        if self.isFull():
            raise Exception("Queue is full.")
        else:
            self.dqueue.insert(0, element)

    def deleteRear(self):
        '''
        Deletes an element from the back of the queue.
        :param: None.
        :returns: element
        :rtype: object.
        '''
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.dqueue.pop()
    
    def deleteFront(self):
        '''
        Deletes an element from the front of the queue.
        :param: None.
        :returns: element
        :rtype: object.
        '''
        if self.isEmpty():
            raise Exception("Queue is empty.")
        else:
            return self.dqueue.pop(0)
    
    def display(self):
        '''
        Displays all the elements from the queue.
        :param: None.
        :retunrs : None.
        :rtype: None
        '''
        if self.isEmpty():
            raise Exception("Queue is empty.")
        else:
            print("|", end="")
            for element in self.dqueue:
                print("{}".format(element), end="|")
            print()

    def rearPeek(self):
        '''
        Displays the last element from the back of the queue
        :param: None.
        :returns: element.
        : rtype: object.
        '''
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.dqueue[-1]
        
    def frontPeek(self):
        '''
        Displays the first element from the front of the queue.
        :param: None.
        :returns : element.
        :rtype: object.
        '''
        if self.isEmpty():
            raise Exception("Queue is emepty")
        else:
            return self.dqueue[0]
        
    
q = Dqueue(5)
q.addRear("A")
q.addFront("B")
q.addRear("C")
q.display()
print(q.rearPeek())
print(q.frontPeek())