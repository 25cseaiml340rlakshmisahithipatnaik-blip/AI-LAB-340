"""Experiment 8: Solve the water-jug problem using BFS."""
from collections import deque
from math import gcd


def water_jug(capacity1, capacity2, target):
    if target < 0 or target > max(capacity1, capacity2):
        return None
    if target == 0:
        return [(0, 0)]
    if gcd(capacity1, capacity2) == 0 or target % gcd(capacity1, capacity2) != 0:
        return None
    queue = deque([((0, 0), [(0, 0)])])
    visited = {(0, 0)}
    while queue:
        (jug1, jug2), path = queue.popleft()
        if jug1 == target or jug2 == target:
            return path
        pour12 = min(jug1, capacity2 - jug2)
        pour21 = min(jug2, capacity1 - jug1)
        next_states = [
            (capacity1, jug2), (jug1, capacity2), (0, jug2), (jug1, 0),
            (jug1 - pour12, jug2 + pour12),
            (jug1 + pour21, jug2 - pour21),
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None


def main():
    jug1 = int(input("Enter capacity of jug 1: "))
    jug2 = int(input("Enter capacity of jug 2: "))
    target = int(input("Enter target amount: "))
    if jug1 <= 0 or jug2 <= 0:
        print("Jug capacities must be positive.")
        return
    solution = water_jug(jug1, jug2, target)
    if solution is not None:
        print("\nSteps to reach the target:")
        for step in solution:
            print(step)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
