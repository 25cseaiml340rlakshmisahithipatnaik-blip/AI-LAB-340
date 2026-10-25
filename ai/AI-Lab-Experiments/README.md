# AI Lab Experiments — Python

This repository contains 10 AI lab programs, each in its own folder with source code and a sample run. The code is organized for a student lab submission and retains the experiments' intended topics while fixing obvious execution or algorithm issues.

## Experiments

| No. | Experiment | Source file |
|---:|---|---|
| 1 | Breadth-First Search (BFS) | `Experiment-01-BFS/bfs.py` |
| 2 | Depth-First Search (DFS) | `Experiment-02-DFS/dfs.py` |
| 3 | Hill Climbing | `Experiment-03-Hill-Climbing/hill_climbing.py` |
| 4 | A* Search | `Experiment-04-A-Star/a_star.py` |
| 5 | Minimax | `Experiment-05-Minimax/minimax.py` |
| 6 | Alpha-Beta Pruning | `Experiment-06-Alpha-Beta-Pruning/alpha_beta.py` |
| 7 | 8-Queens Problem | `Experiment-07-Eight-Queens/eight_queens.py` |
| 8 | Water-Jug Problem | `Experiment-08-Water-Jug/water_jug.py` |
| 9 | Tic-Tac-Toe | `Experiment-09-Tic-Tac-Toe/tic_tac_toe.py` |
| 10 | Travelling Salesman Problem (TSP) | `Experiment-10-Travelling-Salesman/tsp.py` |

## Requirements

- Python 3.9 or later recommended.
- No third-party packages are required; all programs use Python's standard library.

## Run an experiment

1. Download or clone this repository.
2. Open a terminal in the desired experiment folder.
3. Run the source file with Python. For example:

```bash
cd Experiment-01-BFS
python bfs.py
```

4. Enter the requested values. Compare the result with `sample_output.txt`.

## Notes

- Graph inputs for BFS and DFS are treated as undirected. A* accepts directed edges and non-negative costs.
- Minimax expects a complete binary game tree, so the number of leaf values must be a power of two.
- Alpha-Beta Pruning uses exactly eight leaf values (a depth-3 binary tree).
- TSP uses exhaustive permutations and is suitable only for small numbers of cities because its running time grows factorially.
- Sample outputs are text captures of representative runs; prompts may look slightly different depending on the terminal.

## Before submitting

Check your institution's naming and report requirements, review each program so you can explain it during evaluation, and ensure the repository link is accessible to your instructor. This folder has not been pushed to GitHub automatically.
