import random

class BubbleSort(object):
    """The class which implements the bubble sort algorithm
    """

    def __init__(self, limit=10):
        """Initialize the list by generating the random numbers
        """
        self.lst_num = self.__generate_random_list(limit)
        
    def __generate_random_list(self, limit):
        """Returns the list of random number between -200 and 500
           The length of the list is specified by limit.
        """
        return [random.randint(-200,500) for i in range(limit)]

    def display(self):
        """Prints the list of numbers
        """
        print(self.lst_num)

    def sort(self):
        """Returns the sorted list after applying the bubble sort algorithm.
        """
        for i in range(len(self.lst_num)):
            for j in range(len(self.lst_num)-1-i):
                if self.lst_num[j] > self.lst_num[j+1]:
                    self.lst_num[j], self.lst_num[j+1] = self.lst_num[j+1], self.lst_num[j]
                    

if __name__ == "__main__":
    # Initialization of the bubble sort class to bbs object
    bbs = BubbleSort()
    print("Before sorting the list elements are:")
    bbs.display()
    bbs.sort()
    print("After sorting with Bubble Sort Algorithm, the list elements are:")
    bbs.display()