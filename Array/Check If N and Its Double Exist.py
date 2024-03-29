"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3

"""


def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """

    arr = sorted(arr, key=lambda x: abs(x))
    n = len(arr)
    j = n - 1
    i = 0
    for i in range(n):
        if (arr[i] * 2 in arr[i + 1:]):
            return True

    return False


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = set(arr)
        for i in s:
            if 2*i in s and i != 0:
                return True
        if arr.count(0) >= 2:
            return True
        return False
        # d = {}
        # for i in range(len(arr)):
        #     if arr[i] not in d:
        #         if arr[i]%2 == 0:
        #             d[arr[i]/2] = 1
        #         d[arr[i]*2] = 1
        #     else:
        #             return True
        # return False



print(checkIfExist([-2,0,10,-19,4,6,-8]))