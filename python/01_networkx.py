
"""
Example 1 - create graph with networkx
Author: Dani Ushizima - dushizima@lbl.gov
Source: https://networkx.github.io/documentation/stable/tutorial.html
"""

import networkx as nx
G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3])
