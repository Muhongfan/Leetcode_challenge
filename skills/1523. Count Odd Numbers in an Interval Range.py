"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).



Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            #      low = low+1
            # ans = []
            # while low <= high:
            #     #print(low)
            #     low = low+2
            #     ans.append(low)
            # reutrn ans
            return (high - low + 1) // 2
        return (high - low) // 2 + 1
