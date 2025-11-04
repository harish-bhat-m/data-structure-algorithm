class SubStringWithoutRepeat:
    def __init__(self, string):
        self.string = string

    def calculate_substring_without_repeat(self):
        char_set = set()
        left = 0
        result = 0

        for right in range(len(self.string)):
            print(f"right:{right}----{self.string[right]}")
            print(char_set)
            while self.string[right] in char_set:
                char_set.remove(self.string[left])
                left += 1
                print(char_set)
            char_set.add(self.string[right])
            result = max(result, right - left + 1)
        return result

if __name__ == "__main__":
    string = input("Enter the string:")
    obj = SubStringWithoutRepeat(string)
    no_str_without_repeat = obj.calculate_substring_without_repeat()
    print(f"The string is '{string}' and nuber of substring without repeat is {no_str_without_repeat}")



