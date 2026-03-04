class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, node, weight=1):
        self.neighbors[node] = weight
   

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)

    def add_edge(self, u, v, weight=1):
        self.add_node(u)
        self.add_node(v)

        self.nodes[u].add_neighbor(self.nodes[v], weight)
                

       