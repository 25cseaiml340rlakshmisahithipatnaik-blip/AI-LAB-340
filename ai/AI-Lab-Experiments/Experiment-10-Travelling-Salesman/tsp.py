"""Experiment 10: Travelling Salesman Problem by exhaustive search."""
from itertools import permutations


def travelling_salesman(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)
    min_cost = float("inf")
    best_path = None
    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        current = start
        for city in perm:
            current_cost += graph[current][city]
            current_path.append(city)
            current = city
        current_cost += graph[current][start]
        current_path.append(start)
        if current_cost < min_cost:
            min_cost, best_path = current_cost, current_path
    return best_path, min_cost


def main():
    n = int(input("Enter the number of cities: "))
    if n < 2:
        print("Enter at least 2 cities.")
        return
    print("Enter the cost matrix (one row per line):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i}: ").split()))
        if len(row) != n:
            print(f"Each row must contain exactly {n} values.")
            return
        graph.append(row)
    start = int(input(f"Enter the starting city (0 to {n - 1}): "))
    if start not in range(n):
        print("Invalid starting city.")
        return
    path, cost = travelling_salesman(graph, start)
    print("\nOptimal Path:", " -> ".join(map(str, path)))
    print("Minimum Cost:", cost)

if __name__ == "__main__":
    main()
