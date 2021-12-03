import random

from matplotlib.pyplot import connect

class Graph:
    graph = []
    edge_set = []
    node_number = 20

    def __init__(self):
        self.graph = []
        for _ in range(0, self.node_number):
            self.graph.append([0] * self.node_number)
        self.generate_random_edges()
        print(self.edge_set)

    def generate_random_edges(self):
        edges_nmb = 20
        
        for _ in range(0, edges_nmb):
            strt = random.randint(0, self.node_number -1)
            end = random.randint(0, self.node_number -1)
            while strt == end or (strt, end) in self.edge_set:
                strt = random.randint(0, self.node_number -1)
                end = random.randint(0, self.node_number -1)
            self.graph[strt][end] = 1
            self.graph[end][strt] = 1
            self.edge_set.append((strt, end))
            self.edge_set.append((end, strt))

    def to_adjacency_list(self):
        adj_list = []

        for i in range(0, self.node_number):
            l = self.graph[i]
            sublist = []
            for n in range(0, len(l)):
                if l[n] == 1:
                    sublist.append(n)
            adj_list.append(sublist)

        return adj_list

    def find_connected_vertices(self, v1: int, connected = []) -> list:
        adj_list = self.to_adjacency_list()
        connected.append(v1)
        adjacents = adj_list[v1]
        for a in adjacents:
            if a in connected:
                continue
            connected = self.find_connected_vertices(a, connected)
        return connected


    def find_connected_components(self) -> list:
        components = []
        visited = []
        for n in range(0, self.node_number):
            if not n in visited:
                comp = self.find_connected_vertices(n, [])
                components.append(comp)
                components = components
                visited = visited + comp
        return components

    def find_node_path(self, v1: int, v2: int, searched = []) -> list:
        adj_list = self.to_adjacency_list()
        searched.append(v1)

        adjacents = adj_list[v1]
        if v2 in adjacents:
            searched.append(v2)
            return searched
        for adj in adjacents:
            if (adj in searched):
                continue
            return self.find_node_path(adj, v2, searched)
        return []

    def BFS(self, strt, dest, v, pred = {}, dist = {}):
        adjacency_list = self.to_adjacency_list()
        queue = []

        visited = []
  
        visited.append(strt)
        dist[strt] = 0
        queue.append(strt)
  
        while (len(queue) != 0):
            u = queue.pop(0)
            for elem in adjacency_list[u]:
         
                if (not elem in visited):
                    visited.append(elem)
                    dist[elem] = dist[u] + 1
                    pred[elem] = u
                    queue.append(elem)
  

                    if (elem == dest):
                        return True
        return False