import os
import re
import folium


def safe_filename(text):
    return re.sub(r'[<>:"/\\|?*]', '_', str(text))


def save_route_map(
        G,
        path,
        asal,
        tujuan,
        distance
):

    output_dir = (
        "TugasBesar_Algoritma Djikstra/output"
    )

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    coords = []

    for node in path:

        coords.append([
            G.nodes[node]["y"],
            G.nodes[node]["x"]
        ])

    center = coords[0]

    m = folium.Map(
        location=center,
        zoom_start=13,
        control_scale=True
    )

    # =========================
    # NAVBAR
    # =========================

    navbar = """
    <div style="
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:70px;
        background:white;
        z-index:9999;
        display:flex;
        align-items:center;
        padding-left:20px;
        font-size:32px;
        font-weight:bold;
        box-shadow:0 2px 10px rgba(0,0,0,0.3);
    ">
        🗺️ NMaps
    </div>
    """

    m.get_root().html.add_child(
        folium.Element(navbar)
    )

    # =========================
    # INFO CARD
    # =========================

    node_count = len(path)

    estimated_time = (
        distance / 40
    ) * 60

    info_card = f"""
    <div style="
        position:fixed;
        top:100px;
        right:20px;
        width:320px;
        background:white;
        z-index:9999;
        border-radius:12px;
        padding:20px;
        box-shadow:0 4px 15px rgba(0,0,0,0.3);
        font-family:Arial;
    ">

    <h2 style="margin-top:0;">
    📍 Informasi Rute
    </h2>

    <hr>

    <p>
    <b>Asal</b><br>
    {asal}
    </p>

    <p>
    <b>Tujuan</b><br>
    {tujuan}
    </p>

    <p>
    <b>Jarak</b><br>
    {distance:.2f} km
    </p>

    <p>
    <b>Estimasi Waktu</b><br>
    {estimated_time:.0f} menit
    </p>

    <p>
    <b>Jumlah Node</b><br>
    {node_count}
    </p>

    <p>
    <b>Algoritma</b><br>
    Bidirectional Dijkstra
    </p>

    </div>
    """

    m.get_root().html.add_child(
        folium.Element(info_card)
    )

    # =========================
    # MARKER AWAL
    # =========================

    folium.Marker(
        location=coords[0],
        popup=f"Asal : {asal}",
        icon=folium.Icon(
            color="green",
            icon="play"
        )
    ).add_to(m)

    # =========================
    # MARKER TUJUAN
    # =========================

    folium.Marker(
        location=coords[-1],
        popup=f"Tujuan : {tujuan}",
        icon=folium.Icon(
            color="red",
            icon="flag"
        )
    ).add_to(m)

    # =========================
    # GARIS RUTE
    # =========================

    folium.PolyLine(
        coords,
        color="blue",
        weight=6,
        opacity=1
    ).add_to(m)

    # =========================
    # AUTO FIT
    # =========================

    m.fit_bounds(coords)

    # =========================
    # NAMA FILE OTOMATIS
    # =========================

    asal_file = safe_filename(asal)
    tujuan_file = safe_filename(tujuan)

    output_file = os.path.abspath(
        os.path.join(
            output_dir,
            f"Rute[{asal_file}]-[{tujuan_file}].html"
        )
    )
    # ========================= 
    # SAVE
    # =========================

    m.save(output_file)

    print(
        f"Map berhasil disimpan : {output_file}"
    )

    return output_file