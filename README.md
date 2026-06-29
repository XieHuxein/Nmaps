
# Nmaps — Navigation Maps
A route-finding system using the Bidirectional Dijkstra algorithm.

## Project Description

Nmaps is a route optimization application that finds the shortest path using the **Bidirectional Dijkstra** algorithm with road network data from OpenStreetMap (OSM).

This application can:

- Find the shortest route from a starting point to a destination
- Use Jakarta road network data in GraphML format
- Support route search based on location names / POIs
- Display route results on an interactive HTML map
- Show route information such as:
  - Starting point
  - Destination
  - Total distance
  - Number of traversed nodes

---

## Team Members

- At’Thoriq Huseini Subakuh
- Walada Hulama Zaky
- Danang Nur Rizq
- Rizky Hendrawan

---

## Project Structure

```bash
Nmaps/
│
├── data/
│   ├── jakarta.graphml
│   └── poi_jakarta.json
│
├── output/
│
├── app.py
├── graph_loader.py
├── geocoder.py
├── route_finder.py
├── map_visualizer.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3.13 (recommended)
- OpenStreetMap
- OSMnx
- NetworkX
- Folium
- Bidirectional Dijkstra

---

## Installation

### 1. Clone or Download the Project

Extract or clone the project into your local directory.

### 2. Install Python

Recommended versions:

- Python 3.13
- Python 3.14

Check Python version:

```bash
python --version
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Program

Navigate to the project directory:

```bash
cd Nmaps
```

Run:

```bash
python app.py
```

---

## Usage

The program will ask for input:

```text
Origin:
Destination:
```

Example:

```text
Origin: Monumen Nasional
Destination: Stasiun Klender
```

After processing:

- The route will be calculated
- An HTML file will be generated inside the output folder
- The browser will open automatically

Example output:

```text
Graph loaded: 93736 nodes, 215785 edges
Distance: 11.97 km
Map successfully generated
```

---

## Algorithm

### Bidirectional Dijkstra

Advantages:

- Faster than standard Dijkstra
- Performs search from two directions:
  - From source
  - From target
- More efficient for large graph datasets

---

## Dataset Setup

The Jakarta GraphML dataset is compressed due to GitHub file size limitations.

Steps:
1. Extract `data/jakarta.zip`
2. Ensure the extracted file is placed at:

data/jakarta.graphml

Data sources:

- OpenStreetMap (Jakarta road network)
- Jakarta POI (Points of Interest)

Dataset includes:

- Roads
- Intersections
- Landmarks
- Monuments
- Stations
- Public places

---

## Program Output

Output is an interactive HTML file.

Example:

```text
Route_[Monumen Nasional]_[Stasiun Klender].html
```

Map features:

- Route polyline
- Origin marker
- Destination marker
- Nmaps navigation bar
- Route information sidebar

---

## Notes

If you encounter this error:

```text
ImportError: scikit-learn must be installed
```

Install manually:

```bash
pip install scikit-learn
```

If the browser does not open automatically, open the generated HTML file manually from the output folder.

