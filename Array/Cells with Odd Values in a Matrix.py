"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.



Example 1:


Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:


Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.


Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m

"""
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        a=[[0 for i in range(m)] for j in range(n)]
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        for item in indices:
            x,y=item
            for dirs in direction:
                x1,y1=x,y
                while(x1>=0 and x1<n and y1>=0 and y1<m):
                    a[x1][y1]+=1
                    x1+=dirs[0]
                    y1+=dirs[1]
            a[x][y]-=2
        cnt=0
        for i in range(n):
            for j in range(m):
                if(a[i][j]%2==1):
                    cnt+=1
        return cnt

    def oddCells(self, n, m, indices):

        r = []
        c = []
        for [i, j] in indices:
            if i in r:
                r.remove(i)
            else:
                r.append(i)
            if j in c:
                c.remove(j)
            else:
                c.append(j)
        return (len(r) * m + len(c) * n - 2 * len(r) * len(c))