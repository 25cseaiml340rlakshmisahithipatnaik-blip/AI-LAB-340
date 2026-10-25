"""Experiment 3: Hill-climbing search for a maximum."""

def objective_function(x):
    return -4 * (x - 5) ** 2 + 100


def hill_climbing(start, step_size, max_iterations):
    if step_size <= 0:
        raise ValueError("Step size must be positive.")
    current = start
    current_value = objective_function(current)
    for _ in range(max_iterations):
        left, right = current - step_size, current + step_size
        left_value, right_value = objective_function(left), objective_function(right)
        if left_value > current_value and left_value >= right_value:
            current, current_value = left, left_value
        elif right_value > current_value:
            current, current_value = right, right_value
        else:
            break
    return current, current_value


def main():
    start = float(input("Enter starting value: "))
    step_size = float(input("Enter step size: "))
    max_iterations = int(input("Enter maximum iterations: "))
    best_position, best_value = hill_climbing(start, step_size, max_iterations)
    print("Best position:", best_position)
    print("Maximum value:", best_value)

if __name__ == "__main__":
    main()
