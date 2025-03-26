# Algorithm Examples

This document provides practical examples of using the local search algorithms implemented in this project.

## 1. Hill Climbing Examples

### Basic Hill Climbing for 8-Puzzle
```python
from src.puzzle8.puzzle import EightPuzzle
from src.local_search.hill_climbing import hill_climbing

# Create a simple 8-puzzle instance
initial_state = [1, 2, 3,
                4, 0, 5,
                6, 7, 8]
puzzle = EightPuzzle(initial_state)

# Run hill climbing with default parameters
solution, path, metrics = hill_climbing(puzzle)

# Print results
print(f"Solution found: {solution}")
print(f"Path length: {len(path)}")
print(f"Number of steps: {metrics['steps']}")
print(f"Time taken: {metrics['time']:.2f} seconds")
```

### Hill Climbing with Custom Parameters
```python
# Run hill climbing with custom maximum iterations
solution, path, metrics = hill_climbing(puzzle, max_iterations=2000)

# Analyze the solution quality
if puzzle.is_goal(solution):
    print("Found optimal solution!")
else:
    print(f"Found local optimum with value: {puzzle.get_value(solution)}")
```

## 2. Simulated Annealing Examples

### Basic Simulated Annealing for 8-Queens
```python
from src.queens8.queens import EightQueens
from src.local_search.simulated_annealing import simulated_annealing

# Create an 8-queens instance
queens = EightQueens()

# Define a simple temperature schedule
def linear_schedule(t):
    return max(0.01, 1.0 - 0.001 * t)

# Run simulated annealing
solution, path, metrics = simulated_annealing(queens, linear_schedule)

# Print results
print(f"Final board configuration: {solution}")
print(f"Number of conflicts: {queens.get_conflicts(solution)}")
print(f"Steps taken: {metrics['steps']}")
```

### Advanced Simulated Annealing
```python
# Define an exponential cooling schedule
def exponential_schedule(t):
    return 1.0 * (0.95 ** t)

# Run with different parameters
solution, path, metrics = simulated_annealing(
    queens,
    exponential_schedule,
    max_iterations=5000
)

# Analyze solution quality
if queens.is_solution(solution):
    print("Found valid solution with no conflicts!")
    print(f"Solution found in {metrics['steps']} steps")
    print(f"Time taken: {metrics['time']:.2f} seconds")
```

## 3. Comparing Algorithms

```python
import time

def compare_algorithms(puzzle):
    # Hill Climbing
    start_time = time.time()
    hc_solution, hc_path, hc_metrics = hill_climbing(puzzle)
    hc_time = time.time() - start_time
    
    # Simulated Annealing
    start_time = time.time()
    sa_solution, sa_path, sa_metrics = simulated_annealing(
        puzzle,
        lambda t: 1.0 / (1 + t)
    )
    sa_time = time.time() - start_time
    
    print("Hill Climbing Results:")
    print(f"- Solution quality: {puzzle.get_value(hc_solution)}")
    print(f"- Steps taken: {hc_metrics['steps']}")
    print(f"- Time: {hc_time:.2f}s\n")
    
    print("Simulated Annealing Results:")
    print(f"- Solution quality: {puzzle.get_value(sa_solution)}")
    print(f"- Steps taken: {sa_metrics['steps']}")
    print(f"- Time: {sa_time:.2f}s")
```

## 4. Visualization Example

```python
from src.plot_results import plot_solution_path

# Generate and plot a solution path
def visualize_solution(problem, path):
    plot_solution_path(
        path,
        title="Solution Path Visualization",
        save_path="figures/solution_path.png"
    )
```

These examples demonstrate the basic usage of the algorithms and various ways to analyze and visualize the results. For more detailed information about the API, please refer to the API documentation. 