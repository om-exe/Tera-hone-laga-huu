import pylab as plt
import networkx as nx
D=nx.DiGraph()
D.add_weighted_edges_from[[('A','B',1),('C','A',1),('B','C',1)]]
print(nx.pagerank(D))
nx.draw(D,with_labels=True)
plt.show()