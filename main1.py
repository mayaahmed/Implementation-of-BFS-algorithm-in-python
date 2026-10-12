# BFS algorithm
# prints out nodes with their distances from the source and the parent node
import math

"""
    Given adjacency list of graph:     
    s  : r, w 
    r  : v,s 
    t  : w, x, u 
    u  : t, x, y 
    v  : r 
    w  : s, t, x 
    x  : w, t, u, y 
    y  : x, u

    """

def main():
    # initial step
    # color attribute is not required for the program
    # Convert graph to a dictionary of dictionaries

    graph = {'s': {'node': 's', 'adjacency_list': ['r', 'w'], 'distance': math.inf, 'parent': None}, 
             'r': {'node': 'r', 'adjacency_list': ['v', 's'], 'distance': math.inf, 'parent': None}, 
             't': {'node': 't', 'adjacency_list': ['w', 'x', 'u'], 'distance': math.inf, 'parent': None}, 
             'u': {'node': 'u', 'adjacency_list': ['t', 'x', 'y'], 'distance': math.inf, 'parent': None}, 
             'v': {'node': 'v', 'adjacency_list': ['r'], 'distance': math.inf, 'parent': None},
             'w': {'node': 'w', 'adjacency_list': ['s', 't', 'x'], 'distance': math.inf, 'parent': None}, 
             'x': {'node': 'x', 'adjacency_list': ['w', 't', 'u', 'y'], 'distance': math.inf, 'parent': None}, 
             'y': {'node': 'y', 'adjacency_list': ['x', 'u'], 'distance': math.inf, 'parent': None}}

    source = graph['s']
    graph = bfs(graph, source)
    print(graph)


def bfs(graph, source):
    #initial steps 
    queue = []     #Initialize a queue
    visited = [] # List to keep track of visited nodes
    source['distance']=0
    queue.append(source)     #Initialize a queue. queue contains nodes with their associated dictionaries
    visited.append(source['node'])  # visited only contains names of nodes

    #First in first out queue
    while queue:
        u = queue.pop(0) 
        print(f"node: {u['node']} -  distance: {u['distance']}, parent: {u['parent']}") # print the nodes with their attributes
        # Look at  all the nodes adjacent to u
        for  v in u['adjacency_list']:
                if v not in visited:
                    graph[v]['distance'] = u['distance']+1
                    graph[v]['parent'] = u['node']
                    queue.append(graph[v])
                    visited.append(v) 
    return graph


if __name__ == "__main__":
    main()

