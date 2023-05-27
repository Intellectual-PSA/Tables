import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Table1")
G.add_node("Table2")
G.add_node("Pool")

G.add_edge("Table1", "Table2")
G.add_edge("Table1", "Pool")

nx.draw(G, with_labels=True)
plt.show()
