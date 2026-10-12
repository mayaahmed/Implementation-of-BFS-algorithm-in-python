# BFS algorithm
# prints out nodes with their distances from the source and the parent node
import bfs
import graph_file_functions
import draw_graph



def main():
    adj_list = graph_file_functions.get_adjacency_list("graphsource_s.txt")
    graph = graph_file_functions.init_graph(adj_list)
    source = graph['s']
    graph = bfs.bfs(graph, source)
    nodes, edges = draw_graph.get_nodes_edges(adj_list)
    draw_graph.draw_graph(nodes,edges)
     # Get edges of bfs tree
    tree_edges= bfs_tree_edges(graph, source)
    draw_graph.draw_graph(nodes,tree_edges)
   

# Get the bfs  tree edges
# Call this function only after bfs is called
def bfs_tree_edges(graph, source):
    tree_edges=[]
    for node in graph:
        if(node != source) and graph[node]['parent'] != None:
           tree_edges.append((node, graph[node]['parent']))
    return tree_edges

        


if __name__ == "__main__":
    main()

