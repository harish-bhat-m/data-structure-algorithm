""" Implementation to check whether the string input is palindrome or not"""

class Palindrome():
    """ Class implementation"""

    def __init__(self, string):
        self.string = string
        self.result = True

    def display_palindrome_result(self):
        """ Display functionality  to print the palindrome result """
        if self.result:
            print("{0} is palindrome".format(self.string))
        else:
            print("{0} is not palindrome".format(self.string))

    def check_palindrome(self):
        """ Functionality to check the word is palindrome or not"""
        string_length = len(self.string)
        string = self.string.lower()
        for i in range(len(self.string)):
            if string[i] != string[string_length - i - 1]:
                self.result = False
                break

if __name__ == "__main__":
    input_string = input("Enter the string to check the palindrome")
    palindrome = Palindrome(input_string)
    palindrome.check_palindrome()
    palindrome.display_palindrome_result()
