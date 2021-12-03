import random

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
        edges_nmb = 40
        
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

    def backward_read(self, con_map: list, v2: int):
        l = [v2]
        pre = con_map[v2]

        while pre != -1:
            l.append(pre)
            pre = con_map[pre]
        return l

    def find_node_path(self, v1: int, v2: int) -> list:
        print(f'Search between {v1} and {v2}')
        adj_list = self.to_adjacency_list()
        searched = [v1]
        
        con_map = [-1 for _ in range(0, self.node_number)]

        queue = [ (v1, vn) for vn in adj_list[v1]]

        if v1 == v2:
            return []

        while len(queue) > 0:
            parent, elem = queue.pop()
            if not elem in searched:
                searched.append(elem)
                con_map[elem] = parent

                if elem == v2:
                    return self.backward_read(con_map, v2)

                queue =  [ (elem, vn) for vn in adj_list[elem]] + queue
        return []