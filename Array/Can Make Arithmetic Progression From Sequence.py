"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.



Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = sorted(arr)
        diff = s[0] - s[1]
        for i in range(0, len(s),2):
            if diff != s[i - 1] - s[i]:
                return False
        return True