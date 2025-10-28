from collections import Counter
class Anagram:
    """
    Class to check whether the two strings are anagram or not
    """
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def __create_dictionary(self, string):
        """
        Create a dictionary keeping string as key and its
        count in the string as value
        :param string: string to create dictionary
        :return: dictionary
        :rtype: dict
        """
        dict = {}
        for char in string:
            dict[char] = dict.get(char, 0) + 1
        return dict
    
    def check_anagram_one(self):
        """
        Check the anagram using dictionary
        :return: True if anagram else False
        :rtype: bool
        """
        str_dict1 = self.__create_dictionary(self.str1)
        str_dict2 = self.__create_dictionary(self.str2)
        return str_dict1 == str_dict2

    def check_anagram_two(self):
        """
        check the anagram using sorted string
        equality of string. If equal then it is anagram
        :return: True if anagram else False
        :rtype: bool
        """
        return sorted(self.str1) == sorted(self.str2)
    
    def check_anagram_three(self):
        """
        Check the anagram using Counter
        :return: True if anagram else False
        :rtype: bool
        """
        return Counter(self.str1) == Counter(self.str2)
    

if __name__ == "__main__":
    # Input from the user
    str1 = input("Enter the first string to check the anagram:")
    str2 = input("Enter the second string to check the anagram:")

    # Instance of the class
    anagram = Anagram(str1, str2)

    # Check the anagram using pythonic way
    result_one = anagram.check_anagram_one()
    result_two = anagram.check_anagram_two()
    result_three = anagram.check_anagram_three()

    # Check the anagram using non pythonic way
    print("============================================")
    print("Implemented using check_anagram_one method")
    if result_one:
        print(f"'{str1}' and '{str2}' are anagram")
    else:
        print(f"'{str1}' and '{str2}' are not anagram")

    print("--------------------------------------------")
    print("Implemented using check_anagram_two method")
    if result_two:
        print(f"'{str1}' and '{str2}' are anagram")
    else:
        print(f"'{str1}' and '{str2}' are not anagram") 

    
    print("--------------------------------------------")
    print("Implemented using check_anagram_three method")
    if result_three:
        print(f"'{str1}' and '{str2}' are anagram")
    else:
        print(f"'{str1}' and '{str2}' are not anagram")