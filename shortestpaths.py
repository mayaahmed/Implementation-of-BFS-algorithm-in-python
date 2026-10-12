# BFS algorithm
# prints out nodes with their distances from the source and the parent node
#prints out the shortest paths from each node to source
import bfs
import graph_file_functions

def main():
    file = "graphsource_s.txt"
    graph = get_graph(file)
    source = 's'  
    graph = bfs.bfs(graph, graph[source])
    print_shortest_paths(graph, source)


def get_graph(file):
    adj_list = graph_file_functions.get_adjacency_list(file)
    return graph_file_functions.init_graph(adj_list)

# run a recursive function on parents of a node till we reach the source.
def print_path(graph, source, v):
    if v == source:
        print(source,  end="")
    elif graph[v]['parent'] == None:  # v is not reachable from the source
        print(f"no path from {source} to {v} exists" )
    else:
        print_path(graph, source, graph[v]['parent'])
        print(v, end="")


def print_shortest_paths(graph, source):
    for node in graph:
            if(node != source):
                print(f"The shortest path from {source}  to {node}:")
                print_path(graph, source, node)
                print("")


if __name__ == "__main__":
    main()

