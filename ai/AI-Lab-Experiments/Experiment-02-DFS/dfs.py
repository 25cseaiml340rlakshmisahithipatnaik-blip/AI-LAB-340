"""Experiment 2: Depth-First Search (DFS) on an undirected graph."""

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal = []

    while stack:
        current_node = stack.pop()  # LIFO: this is a stack, not a queue
        if current_node in visited:
            continue
        visited.add(current_node)
        traversal.append(current_node)
        print(f"Exploring node: {current_node}")
        # Reverse keeps traversal order intuitive for the entered adjacency list.
        for neighbour in reversed(graph.get(current_node, [])):
            if neighbour not in visited:
                stack.append(neighbour)
    return traversal


def main():
    print("------ Build your graph ------")
    student_graph = {}
    num_edges = int(input("How many edges does your graph have? "))
    print("Enter each edge separated by spaces:")
    for i in range(num_edges):
        u, v = input(f"Edge {i + 1}: ").split()
        student_graph.setdefault(u, []).append(v)
        student_graph.setdefault(v, []).append(u)
    start = input("Enter the starting node for DFS: ").strip()
    print(f"\nYour Graph Dictionary: {student_graph}")
    print("Starting DFS Traversal...")
    if start not in student_graph:
        print(f"Starting node {start!r} is not present in the graph.")
        return
    dfs(student_graph, start)

if __name__ == "__main__":
    main()
