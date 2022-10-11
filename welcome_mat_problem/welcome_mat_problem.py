# Welcome Mat problem
import sys
class Mat(object):
    """Class implmentation for the mat problem"""
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.welcome_text = "WELCOME"
    
    def draw(self):
        count = 1
        for i in range((self.m-1)//2):
            scc = self.n - (count*3)
            ssc_c = scc //2
            print("{}{}{}".format("-"*ssc_c,".|."*count,"-"*ssc_c))
            count +=2
        dash_count = (self.n - 7)//2
        print("{}{}{}".format("-"*dash_count, self.welcome_text,"-"*dash_count))
        for i in range((self.m-1)//2):
            count -=2
            scc = self.n - (count*3)
            ssc_c = scc //2
            print_string = "{}{}{}".format("-"*ssc_c,".|."*count,"-"*ssc_c)
            print(print_string, file=sys.stdout)
            


mat = Mat(11,33)
mat.draw()
