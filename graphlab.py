class Graph:
    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.adj = {}
    
    def add_edge(self, u, v, weight=1):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        if self.weighted:
            self.adj[u].append((v, weight))
        else:
            self.adj[u].append(v)

        if not self.directed:
            if self.weighted:
                self.adj[v].append((u, weight))
            else:
                self.adj[v].append(u)
                

       