"""
https://leetcode.com/problems/find-center-of-star-graph/

There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node andexactly n - 1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
that there is an edge between the nodes ui and vi. Return the center of the give
n star graph.
"""

def findCenter(edges):
    """
    :type edges: List[List[int]]
    :rtype: int
    """

    d = {}
    for pair in edges:
        for vertex in pair:
            if vertex in d:
                d[vertex] += 1
            else:
                d[vertex] = 1

    return max(d, key=d.get)
