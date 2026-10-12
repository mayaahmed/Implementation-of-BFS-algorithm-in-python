# BFS algorithm
# prints out nodes with their distances from the source and the parent node
import bfs
import graph_file_functions

def main():
    file = "graphsource_s.txt"
    graph = get_graph(file)
    source = graph['s']
    graph = bfs.bfs(graph, source)
    print(graph)

def get_graph(file):
    adj_list = graph_file_functions.get_adjacency_list(file)
    return graph_file_functions.init_graph(adj_list)


if __name__ == "__main__":
    main()

