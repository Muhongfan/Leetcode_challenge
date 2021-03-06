"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""

#dfs
def allPathsSourceTarget(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    dfs(graph, 0, res, [0])
    return res


def dfs(graph, start, res, path):
    end = len(graph) - 1
    if start == end:
        res.append(path)
    for node in graph[start]:
        dfs(graph, node, res, path + [node])

print(allPathsSourceTarget([[1,2], [3], [3], []] ))

#demo Solu

def allPathsSourceTargetdemo(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """

    def dfs(cur, path):
        if cur == len(graph) - 1:
            res.append(path)
        else:
            for i in graph[cur]:
                dfs(i, path + [i])

    res = []
    dfs(0, [0])
    return res

#demo Solu2
def allPathsSourceTargetdemo2(graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    ans, end = [], len(graph) - 1

    def dfs(node, path):
        if node == end:
            ans.append(path)
            return

        for child in graph[node]:
            dfs(child, path + [child])

    dfs(0, [0])
    return ans