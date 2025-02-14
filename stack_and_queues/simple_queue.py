# Simple queue implementation in python

class Queue(object):
    '''
    Simple queue implemntation in Python
    A queue is an object (an abstract data structure - ADT) that allows the following operations:

    Enqueue: Add an element to the end of the queue
    Dequeue: Remove an element from the front of the queue
    IsEmpty: Check if the queue is empty
    IsFull: Check if the queue is full
    Peek: Get the value of the front of the queue without removing it    

    '''

    def __init__(self, size_of_queue):
        '''
        Initialization of the queue
        :param size_of_queue: The size of the queue
        :type size_of_queue: int
        :Excpetion ValueError if size_of_queue is not integer
        :return: None
        : Initializes the queue onject
        '''
        try:
            self.size_of_queue = int(size_of_queue)
            self.queue = [None] * self.size_of_queue
            self.head = self.tail = -1
        except ValueError as error:
            print("Error Case : Size of the queue must be integer")

    def isFull(self):
        '''
        Checks if the queue is full
        :returns : True if the queue is full otherwise False
        :rtype: bool
        '''
        if self.tail == self.size_of_queue -1:
            return True
        else:
            return False
        
    def isEmpty(self):
        '''
        Checks if the queue is empty\
        :returns : True if the queue is empty otherwise False
        :rtype: bool
        '''
        if self.head == -1:
            return True
        else:
            return False
        
    def enqueue(self, element):
        '''
        Add an element to the end of the queue.
        :param element:  The element need to be added\
        :type element: object
        :raises the Exception if the queue is full
        '''
        if self.isFull():
            raise Exception("Queue is full")
        elif self.head == -1:
            self.queue[self.tail] = element
            self.head = self.tail = 0
            print("Added {} to the queue".format(element))
        else:
            self.queue[self.tail] = element
            self.tail += 1
            print("Added {} to the queue".format(element))
    
    def dequeue(self):
        ''''
        Removes an top element from the queue
        : returns: the top most object from the queue
        :rtype: object
        : raises Exception if the queue is empty
        '''
        if self.isEmpty():
            raise Exception("Queue is empty")
        elif self.head == self.tail:
            element = self.queue[self.head]
            self.head = self.tail = -1
            return element