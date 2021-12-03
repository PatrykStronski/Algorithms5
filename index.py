from generate_graph import Graph
import matplotlib.pyplot as plt
import networkx as nx

g = Graph()

print('---adjacency matrix---')
for r in g.graph:
    print(r)
print('---adjacency list---')
adj = g.to_adjacency_list()
i = 0
for r in adj:
    print(f'{i}: {r}')
    i += 1

g_nx = nx.Graph(g.edge_set)
nx.draw(g_nx, with_labels = True)
plt.show()

print('Connected components')
print(g.find_connected_components())

print('Node path')
print(g.find_node_path(0,10))