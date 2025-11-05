class MedianTwoList:
    """
    Implemetation of the median of two sorted list  
    """
    def __init__(self, list1: list, list2: list):
        """Initialize the median of two sorted list
           :param: 
               list1: list 1
               list2: list 2
        """
        print("In Initialization")
        self.list1 = list1
        self.list2 = list2

    def find_median(self):
        """
        Method to find the median of the two sorted list
        :param: None
        :returns: median of the two sorted list
        :rtype: float
        :exception: None
        """
        median = 0
        list3 = self.list1 + list2
        list3.sort()
        list3_len = len(list3)

        if list3_len % 2 == 0:
            median = (list3[list3_len //2]+ list3[list3_len //2 - 1]) / 2
        else:
            median = list3[list3_len //2]
        return median

    
if __name__ == "__main__":
    list1 = [1,2,3,4,5,6]
    list2 = [7,8,9]
    median = MedianTwoList(list1, list2)
    median_value  = median.find_median()
    print ("List 1 is {}".format(list1))
    print("List2 is {}".format(list2))
    print("Median is {}".format(median_value))
    
