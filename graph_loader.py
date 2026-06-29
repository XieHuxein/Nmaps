import osmnx as ox


def load_graph():
    # print("Load graph...")

    G = ox.load_graphml(
        "TugasBesar_Algoritma Djikstra/data/jakarta.graphml"
    )

    # print(
    #     f"Graph loaded: {G.number_of_nodes()} nodes, "
    #     f"{G.number_of_edges()} edges"
    # )

    return G