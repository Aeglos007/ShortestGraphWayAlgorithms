import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
list_nodes = [0, 1, 2, 3, 4]
G.add_nodes_from(list_nodes)
G.add_edge(1, 2, weight=2.0)
G.add_edge(2, 1, weight=1.0)
G.add_edge(2, 3, weight=2.0)
G.add_edge(4, 3, weight=4.0)
G.add_edge(0, 4, weight=2.0)
G.add_edge(0, 1, weight=5.0)
G.add_edge(0, 2, weight=3.0)
G.add_edge(1, 3, weight=6.0)
G.add_edge(4, 1, weight=6.0)
G.add_edge(4, 2, weight=10.0)
G.nodes[0]['pos'] = (5, 2)
G.nodes[1]['pos'] = (5, -2)
G.nodes[2]['pos'] = (2, 2)
G.nodes[3]['pos'] = (2, -2)
G.nodes[4]['pos'] = (0, 0)
for _ in range(2):
    for i in range(4):
        if G.has_node(i):
            sp = nx.dijkstra_path(G, source=4, target=i)
            node_pos = nx.get_node_attributes(G, 'pos')
            arc_weight = nx.get_edge_attributes(G, 'weight')
            red_edges = list(zip(sp, sp[1:]))
            node_col = ['white' if not node in sp else 'red' for node in G.nodes()]
            edge_col = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
            nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
            nx.draw_networkx_edges(G, node_pos, edge_color=edge_col)
            nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
            plt.axis('off')
            plt.show()
            print("the shortest way from 4 to ", i, ": ")
            print(sp)
    if G.has_node(3):
        G.remove_node(3)

