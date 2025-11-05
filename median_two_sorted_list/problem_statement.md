Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Approach:
1. Merge the two lists.
2. Sort the merged list
3. Find out the length of the merged list
4. if merged list length when divided by two remains the reminder
    Get the middle element and next to the middle element divide by 2
   else 
    Get the middle element and divide by two