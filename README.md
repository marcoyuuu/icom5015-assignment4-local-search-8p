# University of Puerto Rico at Mayagüez  
### Department of Electrical and Computer Engineering  
#### ICOM5015 - Artificial Intelligence

**Project Title:** Local Search Algorithms for 8-Puzzle and 8-Queens Problems 
**Assignment:** Programming Homework – Chapter 4 (Problem 4.4)  

**Team:** Group M  
- **Marco Yu** (Undergraduate, Computer Science)  
- **Samir Rivera** (Undergraduate, Software Engineering)

**Professor:** J. Fernando Vega Riveros  
**Date:** March 26, 2025  

<p align="center">
  <img src="https://www.uprm.edu/wdt/resources/seal-rum-uprm-1280x1280px.png" alt="UPRM Logo" width="250" height="250">
</p>

---

This project implements and compares various local search algorithms for solving the 8-puzzle and 8-queens problems. It includes implementations of hill climbing (steepest ascent, first choice, and random restart) and simulated annealing (with exponential and linear cooling schedules).

## Project Structure

```
.
├── data/                   # Directory for storing experiment results
│   ├── puzzle_results.csv  # Raw results for 8-puzzle experiments
│   ├── queens_results.csv  # Raw results for 8-queens experiments
│   ├── experiment_results.csv  # Combined results from both problems
│   └── results_summary.csv # Summary statistics
├── figures/               # Directory for storing generated plots
└── src/
    ├── local_search/     # Local search algorithm implementations
    │   └── algorithms.py
    ├── puzzle8/         # 8-puzzle problem implementation
    │   └── generator.py
    ├── queens8/         # 8-queens problem implementation
    │   └── generator.py
    ├── ai_berkeley/     # A* search implementation
    │   └── search.py
    ├── experiments/     # Experiment running code
    │   ├── run_experiments.py  # Main script for running experiments
    │   └── test_run.py
    └── utils/          # Utility functions
        └── plot_results.py
```

## Features

- Implementation of multiple local search algorithms:
  - Hill Climbing (Steepest Ascent)
  - Hill Climbing (First Choice)
  - Hill Climbing (Random Restart)
  - Simulated Annealing (Exponential Schedule)
  - Simulated Annealing (Linear Schedule)

- Two problem domains:
  - 8-Puzzle: Find the optimal sequence of moves to arrange tiles
  - 8-Queens: Place 8 queens on a chessboard without conflicts

- Comprehensive experiment framework:
  - Run multiple instances of each problem
  - Collect detailed metrics (success rate, steps, runtime, value improvement)
  - Generate summary statistics
  - Create visualizations

- Visualization tools:
  - Success rate plots for each problem
  - Average steps plots for each problem
  - Runtime plots for each problem
  - Comparison plots across problems
  - Performance matrix
  - Combined metrics plots

## Installation

1. Clone the repository:
```bash
git clone https://github.com/marcoyu/AI_LocalSearch_8P.git
cd AI_LocalSearch_8P
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

### Running Experiments

To run the local search experiments and generate visualizations:

```bash
python -m src.experiments.run_experiments
```

This will:
1. Run experiments for both 8-puzzle and 8-queens problems
2. Generate summary statistics
3. Create visualizations
4. Save results to the data/ and figures/ directories

### Running Test Experiments

To run experiments with additional error handling and progress reporting:

```bash
python -m src.experiments.test_run
```

## Results

The experiments generate several types of results:

1. Raw Data:
   - `data/puzzle_results.csv`: Individual results for 8-puzzle experiments
   - `data/queens_results.csv`: Individual results for 8-queens experiments
   - `data/experiment_results.csv`: Combined results from both problems
   - `data/results_summary.csv`: Aggregated statistics

2. Visualizations:
   - Success rate plots for each problem
   - Average steps plots for each problem
   - Runtime plots for each problem
   - Comparison plots across problems
   - Performance matrix
   - Combined metrics plots

### Output File Formats

1. **Raw Results CSV Files** (`puzzle_results.csv`, `queens_results.csv`):
   - Problem: Name of the problem ('8-Puzzle' or '8-Queens')
   - Algorithm: Name of the algorithm used
   - Instance: Instance number (0-49)
   - Solution Found: Boolean (True/False)
   - Steps: Number of steps taken
   - Runtime: Time in seconds
   - Initial Value: Starting state evaluation
   - Final Value: Final state evaluation
   - Value Improvement: Final Value - Initial Value

2. **Summary Statistics** (`results_summary.csv`):
   - Problem: Name of the problem
   - Algorithm: Name of the algorithm
   - Solution Rate: Mean of Solution Found
   - Solution Std: Standard deviation of Solution Found
   - Num Instances: Count of instances
   - Avg Steps: Mean number of steps
   - Steps Std: Standard deviation of steps
   - Avg Runtime: Mean runtime
   - Runtime Std: Standard deviation of runtime
   - Avg Value Improvement: Mean improvement in evaluation value
   - Value Improvement Std: Standard deviation of value improvement

### Visualization Parameters

1. **Figure Sizes**:
   - Individual problem plots: 10x6 inches
   - Comparison plots: 15x6 inches
   - Performance matrix: 15x12 inches

2. **Color Scheme**:
   - Hill Climbing (Steepest): #2ecc71 (Green)
   - Hill Climbing (First Choice): #3498db (Blue)
   - Hill Climbing (Random Restart): #e74c3c (Red)
   - Simulated Annealing (Exponential): #f1c40f (Yellow)
   - Simulated Annealing (Linear): #9b59b6 (Purple)

3. **Plot Features**:
   - Error bars showing standard deviation
   - Value labels on top of bars
   - Rotated x-axis labels (45 degrees)
   - Clear titles and axis labels
   - Legend placement optimized for readability

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure you're running commands from the project root directory
   - Check that the virtual environment is activated
   - Verify all required packages are installed

2. **File Not Found Errors**
   - Make sure the data/ and figures/ directories exist
   - Check file permissions
   - Verify you're in the correct working directory

3. **Memory Issues**
   - Reduce the number of instances in experiments
   - Clear memory before running large experiments
   - Monitor system resources during execution

4. **Plot Generation Errors**
   - Check if matplotlib backend is compatible
   - Verify write permissions in figures directory
   - Ensure enough disk space is available

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Review the relevant code in src/experiments/
3. Check the data/ directory for partial results
4. Create an issue in the GitHub repository

## Metrics Collected

For each experiment, the following metrics are collected:
- Solution Found: Whether a solution was found
- Steps: Number of steps taken
- Runtime: Time taken in seconds
- Value Improvement: Improvement in evaluation value
- Initial Value: Starting state evaluation
- Final Value: Final state evaluation

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
