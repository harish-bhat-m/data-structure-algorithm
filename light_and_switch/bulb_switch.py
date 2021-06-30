"""  Implementation of light and switch algorithm. The algorithm calculates the number of
trips required to identify the every light with the switch. It also displays the  labeling  
of switch with light in each trip. 
"""
import random
import sys
from collections import defaultdict

class BulbnSwitch():
    """Class implementation of classic switch and light problem.
       This problem has been generalized
    """
    def __init__(self, count):
        self.count = count
        self.lights = range(1,self.count+1)
        # Assign the switch to the variable
        self.switchs =  [1+i for i in range(self.count)]
        self.light_switch_index = {}
        self.switch_map = defaultdict(lambda : "")
        self.light_map = defaultdict(lambda : "")
        self.zfill_value = 0
        self.__setup_light()

    def __setup_light(self):
        """ Functionality to randomly suffle the bulb in the room and
            Map the index of bulb in the room to switch for assertion purpose\
        """
        if self.count == 0:
            print("Error Case: Switch number cannot be zero")
            sys.exit()
        elif self.count == 1:
            self.num_of_trip = 0
        elif self.count == 2:
            self.num_of_trip = 1
            self.zfill_value = 2
        else:
            self.num_of_trip = len(bin(self.count).replace("0b",""))
            self.zfill_value = self.num_of_trip
        self.lights = random.sample(self.switchs, len(self.switchs))

        for switch in self.switchs:
            self.light_switch_index[switch] = self.lights.index(switch)

        for i in self.switchs:
            self.switch_map[i] = bin(i).replace('0b','').zfill(self.zfill_value)


    def __trip_display(self):
        """ Functionality to display the trip wise mapping of the buib
            Input : None.
            Ouput: Display the mapping.
        """
        for i in range(1, self.count + 1):
            print("Switch {0} :-> {1} || Light {2} :-> {3}".\
                format(i,self.switch_map[i],i, self.light_map[i]))
        print("\n")

    def map_switch_2_light(self):
        """ Fucntion to map the switch to light in each trip"""
        for i in range(self.num_of_trip):
            for key, value in self.switch_map.items():
                idx = self.light_switch_index[key]
                self.light_map[self.lights[idx]] += value[i]
            self.__trip_display()
            
    def display(self):
        """Display function to print the order of switch and lights
           It also displays the number of trips needed to map the light.
        """
        print("Light")
        print(self.lights)
        print("\n")
        print("Switch")
        print(self.switchs)
        print("\n")
        print("Number to trips need to map the switch with bulb is {0}".format(self.num_of_trip))

if __name__ == "__main__":
    try:
        num_switch = int(input("Enter the number of switches:"))
        bns = BulbnSwitch(num_switch)
        bns.display()
        bns.map_switch_2_light()
        bns.display()
    except ValueError as error:
        print("Number of switch must be integer")
