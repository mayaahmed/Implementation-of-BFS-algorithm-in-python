# BFS algorithm
# prints out nodes with their distances from the source and the parent node
import bfs
import graph_file_functions



def main():
    adj_list = graph_file_functions.get_adjacency_list("graphsource_s.txt")
    graph = graph_file_functions.init_graph(adj_list)
    source = graph['s']
    graph = bfs.bfs(graph, source)
    print(graph)

if __name__ == "__main__":
    main()

