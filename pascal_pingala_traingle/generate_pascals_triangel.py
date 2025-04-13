""" Generation of pascal triange """
class Pascal():
    """ Implmentation of Pascal triangle.
        Attributes: row, static_list, level, CONSTANT_SPACE
        Methods: get_level, generate_pascal_triangle
    """
    def __init__(self):
        """Initialization of the class attributes
           :param: None
           :return: None.
           :rtype: None.
           :exception: None.
        """
        self.row = [1]
        self.static_list = [0]
        self.level = 0
        self.CONSTANT_SPACE = 6

    def get_level(self):
        """ Method to get the input from the user.
            :param: None.
            :return: None.
            :rtype: None.
            :Exception: If the input is not integer,returns the value error.
        """
        try:
            self.level = int(input("Enter the triagle level:"))
        except ValueError:
            print("Error Case: Input must be integer")

    def generate_pascal_triangle(self):
        """ Method to generate the triable
            :param: Noen.
            :return : None.
            :rtype: None.
            :exception: None.
        """
        for _ in range(self.level):
            row_string = " ".join(str(element) for element in self.row)
            print("{:^{width}}".format(row_string, width=self.level * self.CONSTANT_SPACE))
            self.row = [left+right for left,right in \
                        zip(self.row+self.static_list, self.static_list+self.row)]

if __name__ == "__main__":
    pascal_obj =Pascal()
    pascal_obj.get_level()
    pascal_obj.generate_pascal_traingle()



