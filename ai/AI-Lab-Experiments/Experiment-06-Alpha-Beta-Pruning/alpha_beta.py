"""Experiment 6: Minimax with alpha-beta pruning."""
import math


def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta, height):
    if depth == height:
        return values[node_index]
    if maximizing_player:
        best = -math.inf
        for i in range(2):
            value = alpha_beta(depth + 1, node_index * 2 + i, False, values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    best = math.inf
    for i in range(2):
        value = alpha_beta(depth + 1, node_index * 2 + i, True, values, alpha, beta, height)
        best = min(best, value)
        beta = min(beta, best)
        if beta <= alpha:
            break
    return best


def main():
    values = list(map(int, input("Enter 8 leaf node values separated by spaces: ").split()))
    if len(values) != 8:
        print("Please enter exactly 8 integer values.")
        return
    result = alpha_beta(0, 0, True, values, -math.inf, math.inf, 3)
    print("\nOptimal Value:", result)

if __name__ == "__main__":
    main()
