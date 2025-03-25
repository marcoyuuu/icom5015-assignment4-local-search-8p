# University of Puerto Rico at Mayagüez  
### Department of Electrical and Computer Engineering  
#### ICOM5015 - Artificial Intelligence

**Project Title:** Local Search Algorithms for 8-Puzzle and 8-Queens Problems 
**Assignment:** Programming Homework – Chapter 4 (Problem 4.4)  

**Team:** Group M  
- **Marco Yu** (Undergraduate, Computer Science)  
- **Samir Rivera** (Undergraduate, Software Engineering)  
- **Lex Feliciano** (Undergraduate, Electrical and Computer Engineering)  
- **Shadiel López** (Undergraduate, Computer Engineering)  

**Professor:** J. Fernando Vega Riveros  
**Date:** March 26, 2025  

<p align="center">
  <img src="https://www.uprm.edu/wdt/resources/seal-rum-uprm-1280x1280px.png" alt="UPRM Logo" width="250" height="250">
</p>

---

This project implements and compares various local search algorithms for solving the 8-Puzzle and 8-Queens problems. It includes implementations of hill climbing (steepest ascent, first-choice, and random restart) and simulated annealing with different cooling schedules.

## Project Structure

```
.
├── data/                   # Directory for storing experiment results
├── figures/               # Directory for storing generated plots
├── src/                   # Source code directory
│   ├── ai_berkeley/      # Berkeley AI search implementation
│   ├── local_search/     # Local search algorithm implementations
│   ├── puzzle8/          # 8-Puzzle problem implementation
│   ├── queens8/          # 8-Queens problem implementation
│   ├── run_experiments.py # Main experiment runner
│   └── test_run.py       # Test script for running experiments
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI_LocalSearch_8P
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project

### Running Experiments

To run the experiments and generate results:

```bash
python -m src.test_run
```

This will:
1. Run experiments on both 8-Puzzle and 8-Queens problems
2. Generate results in the `data/` directory
3. Create visualizations in the `figures/` directory

### Running Individual Components

You can also run specific components of the project:

1. Run only 8-Puzzle experiments:
```python
from src.run_experiments import run_8puzzle_experiments
results = run_8puzzle_experiments(num_instances=50)
```

2. Run only 8-Queens experiments:
```python
from src.run_experiments import run_8queens_experiments
results = run_8queens_experiments(num_instances=50)
```

## Project Components

### Local Search Algorithms

The project implements several local search algorithms:

1. Hill Climbing:
   - Steepest Ascent: Explores all neighbors and selects the best improvement
   - First Choice: Randomly explores neighbors until finding an improvement
   - Random Restart: Performs multiple hill climbing runs from random initial states

2. Simulated Annealing:
   - Exponential Schedule: Temperature decreases exponentially
   - Linear Schedule: Temperature decreases linearly

### Problems

1. 8-Puzzle:
   - Implementation includes Manhattan distance heuristic
   - A* search for optimal solutions
   - Local search with valid move generation

2. 8-Queens:
   - Implementation includes conflict counting
   - Local search with neighbor state generation
   - Solution validation

## Results and Analysis

The experiments generate several types of results:

1. Success Rates: Percentage of instances solved by each algorithm
2. Average Steps: Number of steps taken to reach a solution
3. Runtime: Time taken by each algorithm
4. Optimality Gap: Difference between local search steps and A* optimal steps (for 8-Puzzle)
5. Value Improvement: Improvement in evaluation function value

Visualizations include:
- Success rate comparisons
- Runtime analysis
- Step count analysis
- Optimality gap distribution
- Value improvement distribution

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Berkeley AI course materials for the A* search implementation
- Contributors and maintainers of the project

## Algorithms Implemented

1. **Hill Climbing Variants**
   - Steepest-Ascent: Examines all neighbors and selects the best improvement
   - First-Choice: Selects the first improving neighbor
   - Random-Restart: Performs multiple hill climbing attempts from random starting points

2. **Simulated Annealing**
   - Uses exponential cooling schedule: T(t) = k * exp(-λt)
   - Parameters: k = 20, λ = 0.005
   - Allows escaping local optima through probabilistic acceptance of worse states

## References

[1] S. Russell and P. Norvig, "Artificial Intelligence: A Modern Approach", 4th ed., Chapter 4: Beyond Classical Search.

[2] UC Berkeley AI Project Repository, "aima-python", Berkeley AI Lab.

[3] Yale University CS470 Course Materials, "Search Algorithms".

[4] A. Bainalwar, "8-Queens Problem Using Local Search", YouTube Tutorial.

[5] M. S. Saurabh, "8-Queens Puzzle Implementation", GitHub Repository.

[6] N. Shahabi, "8-Queen Problem Solve with Hill Climbing and Simulated Annealing", GitHub Repository.

[7] J. F. Vega-Riveros, "Heuristic Search and Local Search Algorithms", Class Presentation. 