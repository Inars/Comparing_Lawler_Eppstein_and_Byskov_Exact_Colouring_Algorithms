import networkx as nx
import utils
def eppstein(G):
    X = {}
    for S in utils.subsets_of_graph(G):
        #print("Actual S iteration: "+ str(S))
        # TODO check better naming of remove
        S2 = utils.createGraph(S,G)
        X[str(S2.nodes())] = len(S)
        for I in utils.get_max_independent_set(S2):
            substract = utils.diff(S,I)
            X[str(S)] = min(X[str(S)],X[str(substract)] + 1)
    return X[str(list(G.nodes()))]

correct = 0
wrong = 0
for i in range(1,150):
    G = nx.read_gpickle("data/graph"+'{0:03}'.format(i)+".gpickle")
    x = eppstein(G)
    if x != G.graph["Chromatic number"]:
        print(str(x)+" vs "+str(G.graph["Chromatic number"]))
        print("WRONG:: test/graph"+'{0:03}'.format(i)+".gpickle")
        wrong += 1
    else:
        print("RIGHT:: test/graph"+'{0:03}'.format(i)+".gpickle")
        correct += 1

import itertools as I
def c(n,v):
    for i in range(1,n+1):
        for p in I.product(range(i),repeat=n):
            if(0==len([x for x in v if(p[x[0]]==p[x[1]])])):
                return i

#G = nx.read_gpickle("test/graph022.gpickle")
#A = nx.to_numpy_matrix(G)
#print(A)
#print(c(G.number_of_nodes(), list(G.edges())))
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_size = 500)
#nx.draw_networkx_labels(G, pos)
#nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
#nx.draw_networkx_edges(G, pos, arrows=False)
#plt.show()
#plt.draw()
