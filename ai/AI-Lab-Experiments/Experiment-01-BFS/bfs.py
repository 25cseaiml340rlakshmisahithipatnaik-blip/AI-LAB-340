"""Experiment 1: Breadth-First Search (BFS) on an undirected graph."""

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def main():
    print("----- Build your graph -----")
    student_graph = {}
    num_edges = int(input("How many edges does your graph have? "))
    print("Enter each edge separated by a space:")

    for i in range(num_edges):
        u, v = input(f"Edge {i + 1}: ").split()
        student_graph.setdefault(u, []).append(v)
        student_graph.setdefault(v, []).append(u)

    start = input("Enter the starting node for BFS: ").strip()
    if start not in student_graph:
        print(f"Starting node {start!r} is not present in the graph.")
        return

    print("\nYour graph dictionary:", student_graph)
    print("Starting BFS traversal:")
    bfs(student_graph, start)
    print()

if __name__ == "__main__":
    main()
