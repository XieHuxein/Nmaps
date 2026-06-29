import json
import osmnx as ox

with open(
    "TugasBesar_Algoritma Djikstra/data/poi_jakarta.json",
    "r",
    encoding="utf-8"
) as f:
    POIS = json.load(f)


def get_nearest_node(G, place_name):

    place_name = place_name.lower()

    for poi in POIS:

        name = poi.get("name")

        if not isinstance(name, str):
            continue

        if place_name in name.lower():

            print(f"POI ditemukan: {name}")

            return ox.distance.nearest_nodes(
                G,
                poi["lon"],
                poi["lat"]
            )

    raise Exception(
        f"POI tidak ditemukan: {place_name}"
    )