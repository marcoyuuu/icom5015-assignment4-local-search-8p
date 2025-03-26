# Usage Examples

This document provides practical examples of using the local search algorithms implementation for solving 8-Puzzle and 8-Queens problems.

## Basic Usage

### 1. Solving 8-Puzzle with Hill Climbing

```python
from src.puzzle8.generator import generate_8puzzle_instance, get_manhattan_distance
from src.local_search.algorithms import hill_climbing_steepest

# Generate a random 8-puzzle instance
initial_state = generate_8puzzle_instance()
print("Initial state:")
print_state(initial_state)

# Define evaluation function (negative Manhattan distance for maximization)
evaluate = lambda state: -get_manhattan_distance(state)

# Get valid moves for a state
def get_neighbors(state):
    empty_pos = state.index(0)
    valid_moves = get_valid_moves(empty_pos)
    return [apply_move(state, move) for move in valid_moves]

# Solve using hill climbing
solution = hill_climbing_steepest(initial_state, get_neighbors, evaluate)
print("\nFinal state:")
print_state(solution)
```

### 2. Solving 8-Queens with Simulated Annealing

```python
from src.queens8.generator import generate_8queens_state, count_conflicts, get_neighbors
from src.local_search.algorithms import simulated_annealing, exponential_schedule

# Generate random 8-queens state
initial_state = generate_8queens_state()
print("Initial state:")
print_board(initial_state)

# Define evaluation function (negative conflicts for maximization)
evaluate = lambda state: -count_conflicts(state)

# Create cooling schedule
schedule = exponential_schedule(k=30, lam=0.001)

# Solve using simulated annealing
solution = simulated_annealing(initial_state, get_neighbors, evaluate, schedule)
print("\nFinal state:")
print_board(solution)
```

## Advanced Usage

### 1. Comparing Multiple Algorithms

```python
from src.local_search.algorithms import (
    hill_climbing_steepest,
    hill_climbing_first_choice,
    hill_climbing_random_restart,
    simulated_annealing
)
import time

def compare_algorithms(initial_state, get_neighbors, evaluate):
    algorithms = {
        'Steepest Hill Climbing': hill_climbing_steepest,
        'First-Choice Hill Climbing': hill_climbing_first_choice,
        'Random-Restart Hill Climbing': lambda s, n, e: hill_climbing_random_restart(
            s, n, e, generate_8puzzle_instance
        ),
        'Simulated Annealing': lambda s, n, e: simulated_annealing(
            s, n, e, exponential_schedule()
        )
    }
    
    results = {}
    for name, algo in algorithms.items():
        start_time = time.time()
        solution = algo(initial_state, get_neighbors, evaluate)
        runtime = time.time() - start_time
        
        results[name] = {
            'solution': solution,
            'value': evaluate(solution),
            'runtime': runtime
        }
    
    return results

# Example usage
puzzle = generate_8puzzle_instance()
results = compare_algorithms(puzzle, get_neighbors, evaluate)

for name, result in results.items():
    print(f"\n{name}:")
    print(f"Solution quality: {result['value']}")
    print(f"Runtime: {result['runtime']:.3f} seconds")
```

### 2. Custom Problem Implementation

```python
# Example: Implementing a new problem
class CustomProblem:
    def __init__(self, size):
        self.size = size
        self.state = self.generate_initial_state()
    
    def generate_initial_state(self):
        # Implementation specific to your problem
        pass
    
    def get_neighbors(self, state):
        # Generate neighboring states
        pass
    
    def evaluate(self, state):
        # Evaluation function
        pass

# Using with existing algorithms
problem = CustomProblem(size=10)
solution = hill_climbing_steepest(
    problem.state,
    problem.get_neighbors,
    problem.evaluate
)
```

## Running Experiments

### 1. Basic Experiment

```python
from src.experiments.run_experiments import run_8puzzle_experiments

# Run experiments with custom parameters
results = run_8puzzle_experiments(num_instances=50)

# Print summary statistics
print("\nSuccess Rates:")
success_rates = results.groupby('Algorithm')['Solution Found'].mean() * 100
print(success_rates)

print("\nAverage Steps:")
avg_steps = results.groupby('Algorithm')['Steps'].mean()
print(avg_steps)
```

### 2. Custom Experiment Configuration

```python
from src.experiments.run_experiments import run_8queens_experiments
from pathlib import Path

# Set up directories
data_dir = Path('data')
figures_dir = Path('figures')
data_dir.mkdir(exist_ok=True)
figures_dir.mkdir(exist_ok=True)

# Run experiments with custom configuration
results = run_8queens_experiments(
    num_instances=100,
    save_intermediate=True,
    output_dir=data_dir
)

# Save results
results.to_csv(data_dir / 'custom_experiment_results.csv', index=False)
```

## Visualization Examples

### 1. Basic Plotting

```python
from src.utils.plot_results import plot_results
import pandas as pd

# Load results
results = pd.read_csv('data/experiment_results.csv')

# Create visualizations
plot_results(results, Path('figures'))
```

### 2. Custom Visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

def plot_custom_metrics(results):
    plt.figure(figsize=(12, 6))
    
    # Create custom visualization
    sns.boxplot(data=results, x='Algorithm', y='Value Improvement')
    plt.title('Value Improvement by Algorithm')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('figures/custom_plot.png')
    plt.close()

# Example usage
plot_custom_metrics(results)
```

## Tips and Best Practices

1. **Algorithm Selection**
   - Use simulated annealing for complex problems
   - Use hill climbing for simple problems
   - Use random-restart when quality is important

2. **Parameter Tuning**
   - Adjust cooling schedule based on problem size
   - Increase restarts for better solutions
   - Balance exploration vs. exploitation

3. **Performance Optimization**
   - Cache evaluation results when possible
   - Use efficient data structures
   - Implement parallel processing for multiple runs

4. **Error Handling**
   - Always validate input states
   - Handle timeout conditions
   - Save intermediate results 