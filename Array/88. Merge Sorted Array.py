"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""


def merge1(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    ans = []
    pos1 = pos2 = 0
    if m > n:
        while n:
            if nums1[pos1] >= nums2[pos2]:
                ans.append(nums2[pos2])
                pos2 += 1
            else:
                ans.append(nums1[pos1])
                pos1 += 1
            n-=1
        ans.append(nums2[pos2:])
    else:
        while m:
            if nums1[pos1] >= nums2[pos2]:
                ans.append(nums2[pos2])
                pos2 += 1

            else:
                ans.append(nums1[pos1])
                pos1 += 1
            m -= 1
        for i in nums1[pos1:m]:
            ans.append(i)


    return ans
print(merge1([1,2,3,0,0,0],
3,
[2,5,6],
3))
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
        nums1[i+m] = nums2[i]
    nums1.sort()

"""
Time complexity : \mathcal{O}((n + m)\log(n + m))O((n+m)log(n+m)).

The cost of sorting a list of length xx using a built-in sorting algorithm is \mathcal{O}(x \log x)O(xlogx). Because in this case we're sorting a list of length m + nm+n, we get a total time complexity of \mathcal{O}((n + m) \log (n + m))O((n+m)log(n+m)).

Space complexity : \mathcal{O}(n)O(n), but it can vary.

Most programming languages have a built-in sorting algorithm that uses \mathcal{O}(n)O(n) space.
"""


def merge2(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Set p1 and p2 to point to the end of their respective arrays.
    p1 = m - 1
    p2 = n - 1

    # And move p backwards through the array, each time writing
    # the smallest value pointed at by p1 or p2.
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        pos1 = pos2 = 0
        if m > n:

            while n:
                if nums1[pos1] >= nums2[pos2]:
                    ans.append(nums2[pos2])
                    pos2 += 1
                else:
                    ans.append(nums1[pos1])
                    pos1 += 1
            ans.append(nums2[pos2:])
        return ans
