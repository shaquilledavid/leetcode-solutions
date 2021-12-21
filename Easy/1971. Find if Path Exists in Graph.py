import collections
from collections import deque

"""
https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/

Very helpful YouTube video explaining DFS: https://www.youtube.com/watch?v=a2VkK1zqheY

There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
edge between vertex ui and vertex vi. Every vertex pair is connected by at most
one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start
to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid
path from start to end, or false otherwise.
"""

def validPath(n, edges, start, end):
    """
    :type n: int
    :type edges: List[List[int]]
    :type start: int
    :type end: int
    :rtype: bool
    """
    visited = [False] * (n+1) #a list that keeps track if the node, visitied[i] has been visited
    graph = collections.defaultdict(list) 

    #get the adjacency list
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    dfs(start, graph, visited)
    return visited[end] #see if the end node has been visited. if so, a path exists.


def dfs(start, graph, visited):
    visited[start] = True
    stack = deque()
    stack.append(start)
    
    while len(stack) != 0:
        val = stack.pop()
        neighbours = graph[val] #list of nodes that are connected to this node
        
        for neighbour in neighbours:
            if visited[neighbour] == False:
                stack.append(neighbour)
                visited[neighbour] = True
        #if these neighbour nodes haven't been visited yet, update their status


#test graph
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]    
