# BFS algorithm
# prints out nodes with their distances from the source and the parent node
#prints out the shortest paths from each node to source
import bfs
import graph_file_functions
import draw_graph
import shortestpaths
import bfstree
import sys

def main():
    # Get adjacency list and initialize graph from file 
    # get filename and source from command prompt
    if len(sys.argv) > 1:
        file = sys.argv[1]
        source = sys.argv[2]
    
    adj_list = graph_file_functions.get_adjacency_list(file)
    graph = graph_file_functions.init_graph(adj_list)

    # run bfs algorithm
    graph = bfs.bfs(graph, graph[source])

    #list shortest paths for each node
    shortestpaths.print_shortest_paths(graph, source)

    # draw graph and bfs tree    
    nodes, edges = draw_graph.get_nodes_edges(adj_list)
    draw_graph.draw_graph(nodes,edges)
    # Get edges of bfs tree
    tree_edges= bfstree.bfs_tree_edges(graph, source)
    draw_graph.draw_graph(nodes,tree_edges)
    




if __name__ == "__main__":
    main()

