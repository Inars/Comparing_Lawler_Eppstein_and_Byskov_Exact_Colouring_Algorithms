import matplotlib.pyplot as plt
import networkx as nx
from networkx.generators.random_graphs import erdos_renyi_graph
import grinpy
import random
n = 10
p = 0.6666
i = 1
for _ in range(150):
    p = random.uniform(0.5, 0.95)
    n = random.randint(4,5)
    n = 8
    G = erdos_renyi_graph(n, p)
    if not nx.is_connected(G):
        print("Skipping graph not connected")
        continue
    a = grinpy.chromatic_number(G)
    # chromatic number accesed with G.graph["Chromatic number"]
    G.graph = {'Chromatic number': a}
    nx.write_gpickle(G, "test/graph"+'{0:03}'.format(i)+".gpickle")
    i = i + 1
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_size = 500)
#nx.draw_networkx_labels(G, pos)
#nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
#nx.draw_networkx_edges(G, pos, arrows=False)
#plt.show()
#print(G.graph["Chromatic number"])
#plt.draw()
