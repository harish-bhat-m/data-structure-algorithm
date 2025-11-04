1. Program Name : substring_without_repeat.py
Longest Substring Without Repeating Characters
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Implemented using sliding window algorithm. 
Here we use a for loop to iterate the string. While iterating over the
each element, we go an adding the character into a set, meanwhile we check the next element in the string is already present in the set, if yes, we remove the left most character from the set, we repeat this process until remove all the character from the set. Once we remove the left most character, we add the same character to the right side.
During this process we calculate the number substring without the repeat of the character. 
 