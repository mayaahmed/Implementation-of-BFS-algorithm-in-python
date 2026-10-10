# This program reads a graph from a file and initializes it.
import math

def main():
    graph_file = 'graphsource_s.txt'
    graph = read_and_init_graph(graph_file)
    print(graph)

def read_and_init_graph(graph_file):
    G = get_adjacency_list(graph_file)
    graph = init_graph(G)
    return graph


def get_adjacency_list(graph_file):

    # Get a dictionary of the adjacency list from the file
    G = {}
    with open(graph_file, 'r') as file:
        #For each line in the file separate the node and the list of adjacent nodes
        for line in file:
            node, list = line.split(':')
            node = node.strip()
            list = list.strip()
            if(list):
                adj = list.split(',') #create an array of adjacent list
            else:
                adj = []

            G[node] = adj  # Assign adjacent list to node
    return(G)

   

#create a a graph as a dictionary of dictionaries with initialized distances and parents.
def init_graph(G):
  graph = {}
  for k in G:
    graph[k]={'node':k, 'adjacency_list': G[k], 'distance':math.inf, 'parent':None}
  return (graph)




if __name__ == "__main__":
    main()