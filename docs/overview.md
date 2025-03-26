# Local Search Algorithms for 8-Puzzle and 8-Queens Problems

## Project Overview
This project implements and analyzes local search algorithms for solving two classic AI problems: the 8-Puzzle and 8-Queens problems. The implementation focuses on comparing different local search strategies, including Hill Climbing variants and Simulated Annealing, to understand their effectiveness and trade-offs.

## Problem Description

### 8-Puzzle Problem
The 8-puzzle is a sliding puzzle consisting of a 3×3 grid with 8 numbered tiles and one empty space. The goal is to rearrange the tiles from an initial configuration to reach a specific goal state by sliding tiles into the empty space.

**Goal State:**
```
1 2 3
4 5 6
7 8 0
```

### 8-Queens Problem
The 8-Queens puzzle requires placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. In other words, no two queens should share the same row, column, or diagonal.

## Implemented Algorithms

### Hill Climbing Variants
1. **Steepest Ascent Hill Climbing**
   - Evaluates all neighbors and selects the best improvement
   - Complete neighborhood exploration
   - Can get stuck in local maxima

2. **First-Choice Hill Climbing**
   - Selects the first improving neighbor found
   - Random neighborhood exploration
   - Can escape some local maxima through randomization

3. **Random-Restart Hill Climbing**
   - Multiple runs from random initial states
   - Helps escape local maxima
   - Higher computational cost

### Simulated Annealing
1. **Exponential Cooling Schedule**
   - Temperature decreases exponentially
   - Higher initial exploration, faster convergence

2. **Linear Cooling Schedule**
   - Temperature decreases linearly
   - More gradual exploration-exploitation trade-off

## Project Structure
```
AI_LocalSearch_8P/
├── src/                  # Source code
│   ├── puzzle8/         # 8-Puzzle implementation
│   ├── queens8/         # 8-Queens implementation
│   ├── local_search/    # Search algorithms
│   ├── search/          # A* search implementation
│   ├── experiments/     # Experiment runners
│   └── utils/          # Utility functions
├── docs/                # Documentation
├── data/               # Experimental results
└── figures/            # Generated plots
```

## Resources Used
1. **Berkeley AI Course Materials**
   - Base implementation of search algorithms
   - Problem formulation guidelines

2. **Academic Papers**
   - "Solving 8-Puzzle using A* Algorithm and Local Search Methods"
   - "Empirical Analysis of Local Search Algorithms"

3. **Libraries**
   - NumPy: Numerical computations and array operations
   - Pandas: Data analysis and results processing
   - Matplotlib: Visualization and plotting
   - Seaborn: Enhanced statistical visualizations

## Getting Started
See the [Getting Started Guide](guides/getting_started.md) for installation and basic usage instructions.

## Documentation Structure
- [Algorithm Details](algorithms/README.md): Detailed explanation of implemented algorithms
- [API Reference](api/README.md): Code documentation and API reference
- [Usage Examples](examples/README.md): Code examples and tutorials
- [Results Analysis](results/README.md): Analysis of experimental results 