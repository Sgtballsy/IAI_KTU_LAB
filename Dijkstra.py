
def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in graph}
    D[start_vertex] = 0

    unvisited_vertices = list(graph.keys())

    while unvisited_vertices:
        min_vertex = None
        for vertex in unvisited_vertices:
            if min_vertex is None:
                min_vertex = vertex
            elif D[vertex] < D[min_vertex]:
                min_vertex = vertex

        for neighbour, weight in graph[min_vertex].items():
            if weight + D[min_vertex] < D[neighbour]:
                D[neighbour] = weight + D[min_vertex]

        unvisited_vertices.remove(min_vertex)

    return D

def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    for _ in range(num_vertices):
        vertex = input("Enter the vertex: ")
        graph[vertex] = {}
        num_edges = int(input(f"Enter the number of edges for vertex {vertex}: "))
        for _ in range(num_edges):
            edge = input("Enter the edge and weight (format: vertex weight): ").split()
            graph[vertex][edge[0]] = int(edge[1])

    start_vertex = input("Enter the start vertex: ")
    distances = dijkstra(graph, start_vertex)

    print("Shortest distances from start vertex:")
    for vertex, distance in distances.items():
        print(f"Distance to {vertex}: {distance}")

if __name__ == "__main__":
    main()