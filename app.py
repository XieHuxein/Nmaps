from graph_loader import load_graph
from geocoder import get_nearest_node
from route_finder import find_route
from map_visualizer import save_route_map

import time
import os

def main():
    asal = input("Asal : ")
    tujuan = input("Tujuan : ")

    print("Load graph...")
    program_start = time.perf_counter()

    start_load = time.perf_counter()
    G = load_graph()
    end_load = time.perf_counter()
    
    load_time = end_load - start_load
    print(f"Waktu load graph: {load_time:.4f} detik")

    print(
        f"Graph loaded: {G.number_of_nodes()} nodes, "
        f"{G.number_of_edges()} edges"
    )

    print("Cari node asal...")
    source = get_nearest_node(
        G,
        asal
    )

    print("Cari node tujuan...")
    target = get_nearest_node(
        G,
        tujuan
    )

    print("Cari rute...")

    start_route = time.perf_counter()
    distance, path = find_route(
        G,
        source,
        target
    )
    end_route = time.perf_counter()
    route_time = end_route - start_route

    print(f"Waktu pencarian route: {route_time:.4f} detik")

    print(
        f"Jarak : {distance / 1000:.2f} km"
    )

    html_file = save_route_map(
        G,
        path,
        asal,
        tujuan,
        distance / 1000
    )

    print("Selesai")
    
    program_end = time.perf_counter()
    print(f"Total runtime: {program_end - program_start:.4f} detik")

    # otomatis buka html yang baru dibuat
    os.startfile(html_file)


if __name__ == "__main__":
    main()