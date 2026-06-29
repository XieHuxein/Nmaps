import networkx as nx


def find_route(G, source, target):

    path = nx.bidirectional_dijkstra(
        G,
        source,
        target,
        weight="length"
    )

    return path