"""Experiment 4: A* path-finding algorithm for a directed weighted graph."""
import heapq
import itertools


def a_star(graph, heuristic, start, goal):
    counter = itertools.count()
    open_heap = [(heuristic[start], next(counter), start)]
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()

    while open_heap:
        _, _, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        if current == goal:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            print("\nShortest Path:", " -> ".join(path))
            print("Total Cost:", g_cost[goal])
            return path, g_cost[goal]

        closed.add(current)
        for neighbour, cost in graph[current]:
            new_cost = g_cost[current] + cost
            if new_cost < g_cost.get(neighbour, float("inf")):
                g_cost[neighbour] = new_cost
                parent[neighbour] = current
                closed.discard(neighbour)
                heapq.heappush(open_heap, (new_cost + heuristic[neighbour], next(counter), neighbour))

    print("\nNo path found.")
    return None, None


def main():
    graph = {}
    n = int(input("Enter number of nodes: "))
    if n <= 0:
        print("Number of nodes must be positive.")
        return
    nodes = []
    print("\nEnter node names:")
    for i in range(n):
        node = input(f"Node {i + 1}: ").strip()
        if node in graph:
            print("Node names must be unique.")
            return
        nodes.append(node)
        graph[node] = []
    e = int(input("\nEnter number of edges: "))
    print("Enter each directed edge as source, destination, and cost.")
    for i in range(e):
        source = input(f"\nEdge {i + 1} source: ").strip()
        destination = input(f"Edge {i + 1} destination: ").strip()
        cost = int(input("Cost: "))
        if source not in graph or destination not in graph or cost < 0:
            print("Invalid node or negative edge cost.")
            return
        graph[source].append((destination, cost))
    heuristic = {}
    print("\nEnter heuristic values h(n):")
    for node in nodes:
        heuristic[node] = int(input(f"h({node}): "))
    start = input("\nEnter start node: ").strip()
    goal = input("Enter goal node: ").strip()
    if start not in graph or goal not in graph:
        print("Start and goal must be existing nodes.")
        return
    a_star(graph, heuristic, start, goal)

if __name__ == "__main__":
    main()
