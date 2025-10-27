def find_needle_index(stack: str, needle: str) -> int:
    """
    The Pythonic way
    The function to find the index of needle in the haystack.
    :param stack: The haystack
    :type stack: str
    :param needle: The needle
    :type needle: str
    :return: The index of needle in the haystack
    """
    needle_len = len(needle)
    for i in range(len(stack) - needle_len +1):
        if stack[i:i+needle_len] == needle:
            return i
    return -1

def find_needle_index_np(stack: str, needle: str) -> int:
    """
    The non Pythonic way
    The function to find the index of needle in the haystack.
    :param stack: The haystack
    :type stack: str
    :param needle: The needle
    :type needle: str
    :return: The index of needle in the haystack
    """
    stack_len = len(stack)
    needle_len = len(needle)
  
    for i in range(stack_len):
        j = 0
        for k in range(i,stack_len):
            if stack[k] == needle[j]:
                j += 1
            else:
                break

            if j == needle_len:
                    return i
    


if __name__ == "__main__":
    #haystack = input("Enter the phrase for haystack:")
    #needle = input("Now please enter the phrase for needle:")
    haystack = "aSadasaSad"
    needle = "Sad"
    index_py = find_needle_index(haystack, needle)
    index_npy = find_needle_index_np(haystack, needle)
    print(f"The index of needle('{needle}') in haystack('{haystack}') is {index_py}")
    print(f"The index of needle('{needle}') in haystack('{haystack}') is {index_npy}")
