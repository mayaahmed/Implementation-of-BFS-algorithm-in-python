# This program reads a graph from a file and initializes it.
import math

def main():
    graph_file = 'graphsource_s.txt'
    adj_list, graph = read_and_init_graph(graph_file)
    print(adj_list, graph)

def read_and_init_graph(graph_file):
    # Get a dictionary of the adjacency list from the file
    adj_list = get_adj_list(graph_file)
    # Convert the adjacency  list to the initialized  graph 
    graph = init_graph(adj_list)
    return(adj_list, graph)

# convert the adjacency list in the file to a dictionary with the keys as the nodes and the values an array of the adjacency list
def get_adj_list(graph_file):
    G = {}
    with open(graph_file, 'r') as file:
            for line in file:
                node, list = line.split(':')
                node = node.strip()
                list = list.strip()
                if(list):
                    adj = list.split(' ')
                else:
                    adj = []
                G[node] = adj
    return G

#create a a graph as a dictionary of dictionaries with initialized distances and parents.
def init_graph(G):
  graph = {}
  for k in G:
    graph[k]={'node':k, 'adjacency_list': G[k], 'distance':math.inf, 'parent':None}
  return (graph)




if __name__ == "__main__":
    main()