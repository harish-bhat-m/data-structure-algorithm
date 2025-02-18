# This file contains the implmentation of circular queue

class CircularQueue(object):
    '''
    Implmentation of circular queue.
    A circular queue is the extended version of regular queue
    where the last element is connected with the first element.

    Enqueue: Add an element to the end of the queue.
    Dequeue: Remove an element from the front of the queue.
    IsEmpty: Check if the queue is empty.
    IsFull: Check if the queue is full.
    Peek: Get the value of the front of the queue without removing it.
    Display: Displays all the element from the queue.
    '''

    def __init__(self, size_of_queue):
        '''
        Initialization of the circular queue.
        :param: size_of_queue: The size of the queue.
        :rtype: None.
        :return: None.
        :Exception: ValueError if the size_of_queue is not integer.
        '''
        try:
            self.size_of_queue = int(size_of_queue)
            self.queue = [None] * self.size_of_queue
            self.head = self.tail = -1
        except ValueError as error:
            print("Error Case : Size of the queue must be a integer.")

    def isFull(self):
        '''
        Checks the size of the queue is full or not.
        :param: None.
        :returns : True if the queue is full otherwise False.
        :rtype: bool.
        '''
        if ((self.tail + 1) % self.size_of_queue == self.head):
            return True
        else:
            return False
        
    def isEmpty(self):
        '''
        Check the queue is empty or not.
        :param : None.
        :returns: True if the queue is empty otherwise False.
        :rtype: bool.
        '''
        if self.head == -1:
            return True
        else:
            return False
        
    def enqueue(self, element):
        '''
        Adds an element to the circular queue.
        :param: element: The element to be added to the circular queue.
        :returns: None.
        :rtype: None
        Exception: If the queue is full.
        '''
        if self.isFull():
            raise Exception("Queue is full.")
        elif self.head == -1:
            self.head = self.tail = 0
            self.queue[self.tail] = element
        else:
            self.tail = (self.tail + 1 ) % self.size_of_queue
            self.queue[self.tail] = element

    def dequeue(self):
        '''
        Removes first element from the queue.
        :param: None.
        :returns element: The element from the queue.
        :rtype: object.
        :Exception : Raise the exception if the queue is empty.
        '''
        if self.isEmpty():
            raise Exception("Queue is empty.")
        elif self.head == self.tail:
            element = self.queue[self.head]
            self.head = self.tail = -1
            return element
        else:
            element = self.queue[self.head]
            self.head = (self.head + 1 ) % self.size_of_queue
            return element
        
    def display(self):
        '''
        Displays the elements from the circular queue.
        :param: None.
        :returns: None, prints the each element from the circular queue.
        :rtype: None.
        :Exception: Raise the exception if the queue is empty.
        '''
        if self.isEmpty():
            raise Exception("Queeue is empty.")
        elif self.tail >= self.head:
            print("|", end="")
            for element in range(self.head, self.tail + 1):
                print(self.queue[element], end="|")
            print()
        else:
            print("|", end="")
            for element in range(self.head, self.size_of_queue):
                print(self.queue[element], end="|")
            for element in range(0, self.tail + 1):
                print(self.queue[element], end="|")
            print()

    def peek(self):
        '''
        Get the top element of the queue without removing it.
        : returns : top most element from the queue.
        : rtype: object.
        : raises Exception if the queue is empty.
        '''
        if self.isEmpty():
            raise Exception("Queue is empty.")
        else:
            return self.queue[self.head]

if __name__ == "__main__":
    q = CircularQueue(5)
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    q.enqueue("D")
    q.display()
    q.dequeue()
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    
    #q.display()

        
