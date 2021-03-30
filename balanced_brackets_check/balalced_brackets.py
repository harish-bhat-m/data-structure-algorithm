""" Program to check the balaced brackets in an expression """
class BalancedBracket():
    """ Class implementation for balanced bracket check"""

    def __init__(self, expression):
        self.expression = expression
        self.result = 0

    def display_result(self):
        """ Method to display the result of expression"""
        if self.result is False:
            print("The expression '{}' deos not contain any parenthesys".\
                format(self.expression))
        elif self.result == 0:
            print("The expression is '{}' and the brackets are balanced".\
                  format(self.expression))
        else:
            print("The expression is '{}' and the brackets are not balanced".\
                format(self.expression))

    def check_balance_bracket(self):
        """ Method to check the expression's brackets are balalnced or not"""
        expr_flag = 0
        if "(" not in self.expression and ")" not in self.expression:
            self.result = False
        else:
            for charecter in self.expression:
                if charecter == "(":
                    expr_flag += 1
                elif charecter == ")":
                    expr_flag -= 1
                else:
                    continue
            self.result = expr_flag

if __name__ == "__main__":
    objBracket = BalancedBracket(input("Enter the expression:"))
    objBracket.check_balance_bracket()
    objBracket.display_result()
