"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.



Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true


Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1

"""


def kLengthApart(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    left_1 = float("-inf")
    for i, num in enumerate(nums):
        if num == 1:
            if i - left_1 < k + 1:
                return False
            left_1 = i
    return True

def kLengthApart(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    prev = -k - 1
    for i in xrange(len(nums)):
        if not nums[i]:
            continue
        if i - prev <= k:
            return False
        prev = i
    return True

def kLengthApart(self, nums, k):
    if 1 not in nums:
        return True
    first1 = nums.index(1)
    zeroCount = 0
    for index, num in enumerate(nums):
        if index > first1:
            if num == 0:
                zeroCount += 1
            elif num == 1:
                if zeroCount < k:
                    return False
                zeroCount = 0
    return True


