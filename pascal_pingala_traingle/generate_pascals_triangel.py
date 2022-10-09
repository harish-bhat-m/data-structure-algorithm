""" Generation of pascal triange """
class Pascal():
    """ Implmentation of Pascal triangle"""
    def __init__(self):
        self.row = [1]
        self.static_list = [0]
        self.level = 0

    def get_level(self):
        """ Input from the user """
        self.level = int(input("Enter the triagle level:"))

    def generate_pascal_traingle(self):
        """ traingle generation logic"""
        for _ in range(self.level):
            row_string = " ".join(str(element) for element in self.row)
            print("{:^{width}}".format(row_string, width=self.level*6))
            self.row = [left+right for left,right in \
                        zip(self.row+self.static_list, self.static_list+self.row)]

if __name__ == "__main__":
    pascal_obj =Pascal()
    pascal_obj.get_level()
    pascal_obj.generate_pascal_traingle()
