def count_character_change(string: str) -> int:
    """
        Function to count the change in the character in the string.
        :param string: string to count the change in the character.
        :return: count of the change in the character.
        :rtype: int
    """
    if string == "":
        return 0
    else:
        change_count = 0
        previous_character = string[0].lower()

        for character in string[1:]:
            if character.lower() != previous_character:
                change_count += 1
                previous_character = character.lower()
        return change_count
    
if __name__ == "__main__":
    string = input("Enter the string:")
    print(f"The number of character change is {count_character_change(string)}")

