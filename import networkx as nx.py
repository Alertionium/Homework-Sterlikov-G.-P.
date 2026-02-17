import networkx as nx
import matplotlib.pyplot as plt

v = ['A','B','C','D','E']
g = nx.Graph()
g.add_nodes_from(v)
g.add_edge('A','B', weight=1)
g.add_edge('A','C', weight=1)
g.add_edge('A','D', weight=2)
g.add_edge('A','E', weight=3)
g.add_edge('B','E', weight=5)
g.add_edge('C','D', weight=2)
g.add_edge('D','E', weight=4)
pos = nx.spring_layout(g, seed=42)

plt.figure(figsize=(8,6))
nx.draw_networkx_nodes(g, pos, node_color='lightblue', node_size=800)
nx.draw_networkx_edges(g, pos, width=2)
nx.draw_networkx_labels(g, pos, font_size=12)
nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g,'weight'))

plt.axis('off')
plt.show()