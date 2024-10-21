# -*- coding: utf-8 -*-
"""egocenters

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GMOxnNoEH2_sFHu7f0LnGfLJkeMsEPah
"""

import networkx as nx

def find_impostor(edgelist, pseudocenters):
    G = nx.Graph()
    G.add_edges_from(edgelist)

    def get_ego_density(G, node):
        ego_net = nx.ego_graph(G, node)
        num_nodes = len(ego_net.nodes)
        num_edges = len(ego_net.edges)
        if num_nodes > 1:
            possible_edges = num_nodes * (num_nodes - 1) / 2
            return num_edges / possible_edges
        else:
            return 0

    densities = {vertex: get_ego_density(G, vertex) for vertex in pseudocenters if vertex in G.nodes}

    if not densities:
        return None

    impostor = min(densities, key=densities.get)

    return impostor