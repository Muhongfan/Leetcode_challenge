"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = 0
    for elem in nums:
        xor ^= elem
    lowbit = xor & -xor
    a = b = 0
    for num in nums:
        if num & lowbit:
            a ^= num
        else:
            b ^= num
    return [a, b]

print(singleNumber([1,2,1,3,2,5]))



def sinNumber(nums):
    res = []
    dic = {}
    for ele in nums:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] += 1
    for ele in dic:
        if dic[ele] == 1:
            res.append(ele)

    return res