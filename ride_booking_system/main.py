import pandas as pd
import heapq

# Load Drivers
drivers = pd.read_csv("drivers.csv")

# Load Locations
edges = pd.read_csv("locations.csv")

# Build Graph
graph = {}

for _, row in edges.iterrows():
    src = row["source"]
    dest = row["destination"]
    dist = row["distance"]

    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []

    graph[src].append((dest, dist))
    graph[dest].append((src, dist))  # because road is two-way


# Dijkstra Algorithm
def shortest_path(graph, start):
    heap = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# User Location
user_location = input("Enter your location (A/B/C/D/E): ")

# Calculate shortest distance from user
distances = shortest_path(graph, user_location)

# Find Nearest Driver
nearest_driver = None
min_distance = float("inf")

for _, row in drivers.iterrows():
    driver_loc = row["location"]
    driver_dist = distances[driver_loc]

    if driver_dist < min_distance:
        min_distance = driver_dist
        nearest_driver = row["driver_name"]

print("Nearest Driver:", nearest_driver)
print("Distance:", min_distance)