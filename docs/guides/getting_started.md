# Getting Started Guide

## Introduction
This guide will help you get started with the Local Search Algorithms implementation for solving the 8-Puzzle and 8-Queens problems.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_LocalSearch_8P
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix/MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Running Experiments
To run the complete set of experiments:
```bash
python src/run_experiments.py
```

### Visualizing Results
To generate plots and visualizations:
```bash
python src/plot_results.py
```

### Running Individual Problems

#### 8-Puzzle Example
```python
from src.puzzle8.puzzle import EightPuzzle
from src.local_search.hill_climbing import hill_climbing

# Create an 8-puzzle instance
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # 0 represents the empty tile
puzzle = EightPuzzle(initial_state)

# Solve using hill climbing
solution, path, metrics = hill_climbing(puzzle)
```

#### 8-Queens Example
```python
from src.queens8.queens import EightQueens
from src.local_search.simulated_annealing import simulated_annealing

# Create an 8-queens instance
queens = EightQueens()

# Define temperature schedule
def schedule(t):
    return 1.0 / (1 + t)

# Solve using simulated annealing
solution, path, metrics = simulated_annealing(queens, schedule)
```

## Project Structure
```
AI_LocalSearch_8P/
├── src/
│   ├── puzzle8/         # 8-Puzzle implementation
│   ├── queens8/         # 8-Queens implementation
│   └── local_search/    # Search algorithms
├── docs/                # Documentation
├── data/               # Experimental results
└── figures/            # Generated plots
```

## Additional Resources
- Refer to the Jupyter notebook `AI_LocalSearch_Final_Report.ipynb` for detailed analysis
- Check the API documentation in `docs/api/` for detailed function references
- View example code in `docs/examples/` for more use cases 