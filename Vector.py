import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
edges = [
    ('А', 'Б'), ('А', 'В'), ('А', 'Г'), ('А', 'Д'),
    ('Б', 'В'), ('Б', 'Е'),
    ('В', 'Е'), ('В', 'Ж'),
    ('Г', 'В'), ('Г', 'Ж'),
    ('Д', 'Г'), ('Д', 'Ж'), ('Д', 'З'),
    ('Е', 'Ж'), ('Е', 'И'),
    ('Ж', 'И'),
    ('З', 'Ж'), ('З', 'И')
]
G.add_edges_from(edges)
pos = {
    'А': (0, 0), 'Д': (3, 0),
    'Б': (0, -1), 'Г': (2, -1),
    'В': (1, -2), 'Е': (3, -2), 'З': (5, -2),
    'Ж': (2, -3),
    'И': (2, -4),
}

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2500, edgecolors='black')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, 
                       arrowsize=20, arrowstyle='->', width=1.5,
                       connectionstyle='arc3,rad=0.1')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
plt.axis('off')
plt.title("Направленный граф")
plt.tight_layout()
plt.show()

paths = list(nx.all_simple_paths(G, 'А', 'И'))
print(f"Количество путей из А в И: {len(paths)}")