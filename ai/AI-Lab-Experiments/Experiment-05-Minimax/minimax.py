"""Experiment 5: Minimax algorithm for a complete binary game tree."""

def minimax(depth, node_index, is_max, scores, height):
    if depth == height:
        return scores[node_index]
    left = minimax(depth + 1, node_index * 2, not is_max, scores, height)
    right = minimax(depth + 1, node_index * 2 + 1, not is_max, scores, height)
    return max(left, right) if is_max else min(left, right)


def main():
    n = int(input("Enter number of leaf nodes (must be a power of 2): "))
    if n < 2 or n & (n - 1):
        print("The number of leaf nodes must be a power of 2 and at least 2.")
        return
    scores = []
    print("Enter the values of leaf nodes:")
    for i in range(n):
        scores.append(int(input(f"Value {i + 1}: ")))
    height = n.bit_length() - 1
    print("\nOptimal Value:", minimax(0, 0, True, scores, height))

if __name__ == "__main__":
    main()
