# Notebook Improvement Explanations

## Setup and Data Loading

This section initializes the required libraries and loads the experimental results for analysis. We use pandas for data manipulation, matplotlib and seaborn for visualization, and configure the plots to follow IEEE publication standards.

The dataset contains performance metrics for various local search algorithms applied to the 8-Puzzle and 8-Queens problems, including success rates, average steps taken, and average runtime.

## Results Analysis - Success Rates

This visualization compares the success rates of different algorithms across both problems. Success rate represents the percentage of problem instances where the algorithm found the optimal solution. The bar chart shows clear differences in algorithm performance between the two problem domains.

## Performance Metrics

The heatmap visualization provides a comprehensive comparison of key performance metrics (success rates, average steps, and average runtime) for all algorithm-problem combinations. The color intensity indicates the relative performance, with darker colors representing higher values.

## Algorithm Performance Profiles

The radar charts present a normalized view of algorithm performance across multiple metrics for each problem. This visualization allows us to identify algorithms with balanced performance across all metrics versus those that excel in specific areas. The metrics are normalized to a [0,1] scale for fair comparison.

## Implementation Details

### Local Search Algorithms

```python
# Source code from src/local_search/algorithms.py

def hill_climbing_steepest(
    initial_state: List[int],
    get_neighbors: Callable[[List[int]], List[List[int]]],
    evaluate: Callable[[List[int]], float]
) -> Tuple[List[int], List[float]]:
    """
    Steepest-ascent hill climbing implementation.
    
    This algorithm systematically evaluates all neighboring states and moves
    to the neighbor with the highest value. It continues until no better
    neighbor can be found (local optimum).
    
    Args:
        initial_state: The starting state
        get_neighbors: Function to generate neighboring states
        evaluate: Function to evaluate the quality of a state
        
    Returns:
        Tuple of (final state, history of values)
    """
    current_state = initial_state
    current_value = evaluate(current_state)
    value_history = [current_value]
    
    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break
            
        # Find the best neighbor
        best_neighbor = max(neighbors, key=evaluate)
        best_value = evaluate(best_neighbor)
        
        if best_value <= current_value:
            break
            
        current_state = best_neighbor
        current_value = best_value
        value_history.append(current_value)
    
    return current_state, value_history
```

### 8-Puzzle Problem

```python
# Source code from src/puzzle8/generator.py

def get_manhattan_distance(state: Tuple[int, ...], goal: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8)) -> int:
    """
    Calculate the Manhattan distance heuristic for the given state.
    
    Manhattan distance is the sum of the horizontal and vertical distances
    between tiles and their goal positions. This serves as our heuristic
    function for the 8-puzzle problem.
    
    Args:
        state: Current puzzle state as a tuple
        goal: Goal state configuration
        
    Returns:
        The Manhattan distance heuristic value
    """
    distance = 0
    size = 3  # Size of the puzzle grid
    
    for i in range(9):
        if state[i] != 0:  # Skip the blank tile
            current_row = i // size
            current_col = i % size
            
            # Find the goal position of the current number
            goal_idx = goal.index(state[i])
            goal_row = goal_idx // size
            goal_col = goal_idx % size
            
            # Add the Manhattan distance for this tile
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
            
    return distance
```

### 8-Queens Problem

```python
# Source code from src/queens8/generator.py

def count_conflicts(state: Tuple[int, ...]) -> int:
    """
    Count the number of conflicts (attacking pairs) in the current state.
    
    A conflict occurs when two queens can attack each other. This serves
    as our objective function for the 8-queens problem, where we aim to
    minimize the number of conflicts.
    
    Args:
        state: Current board state where index is column and value is row
        
    Returns:
        Number of queen pairs attacking each other
    """
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j]:  # Same row
                conflicts += 1
            elif abs(i - j) == abs(state[i] - state[j]):  # Same diagonal
                conflicts += 1
    return conflicts
```

## Key Findings

This section summarizes the key findings from our experiments:

1. **Algorithm Effectiveness**: Random Restart Hill Climbing consistently outperforms other algorithms across both problems, achieving the highest success rates.

2. **Problem Characteristics**: The 8-Queens problem proved more tractable for local search algorithms compared to the 8-Puzzle problem, with higher success rates across the board.

3. **Simulated Annealing Performance**: The choice of cooling schedule significantly impacts the performance of Simulated Annealing, with the exponential schedule generally providing better results for these problems.

4. **Computational Efficiency**: Hill Climbing variants are computationally more efficient than Simulated Annealing, requiring fewer steps and less runtime to reach solutions.

## Conclusions

Our experiments demonstrate the strengths and limitations of different local search algorithms for solving constraint satisfaction problems:

1. **Random Restart Hill Climbing** provides the best balance between exploration and exploitation, making it the most reliable algorithm for both problems.

2. **Parameter tuning** is crucial for the performance of Simulated Annealing, with cooling schedule selection being particularly important.

3. **Problem structure** significantly influences algorithm performance, highlighting the importance of algorithm selection based on problem characteristics.

4. **Future research** should focus on adaptive parameter selection and hybrid approaches that combine the strengths of multiple algorithms.

## Figure Display

```python
# Display the pre-generated figures from the figures directory
from IPython.display import Image, display

# List of figure files to display
figure_files = [
    'success_rates.png',
    'steps.png',
    'runtimes.png',
    '8puzzle_steps_vs_optimal.png',
    '8puzzle_optimality_gap.png',
    'value_improvements.png',
    'summary_table.png'
]

# Display each figure with a caption
captions = {
    'success_rates.png': 'Figure 1: Success rates of different algorithms across both problems',
    'steps.png': 'Figure 2: Average number of steps taken by each algorithm',
    'runtimes.png': 'Figure 3: Average runtime of each algorithm in seconds',
    '8puzzle_steps_vs_optimal.png': 'Figure 4: Comparison of algorithm steps vs. optimal solution steps for 8-Puzzle',
    '8puzzle_optimality_gap.png': 'Figure 5: Optimality gap analysis for 8-Puzzle solutions',
    'value_improvements.png': 'Figure 6: Improvements in objective function value across algorithms',
    'summary_table.png': 'Figure 7: Summary of performance metrics across all algorithms and problems'
}

for fig_file in figure_files:
    print(captions[fig_file])
    display(Image(filename=f'figures/{fig_file}'))
    print('\n') 