# Local Search Algorithms for 8-Puzzle and 8-Queens Problems

This project implements and compares various local search algorithms to solve the 8-puzzle and 8-queens problems. The implementation includes hill climbing variants (steepest-ascent, first-choice, random-restart) and simulated annealing.

## Project Structure

```
AI_LocalSearch_8P/
├── src/
│   ├── ai_berkeley/     # Berkeley AI Lab search algorithms
│   ├── puzzle8/         # 8-puzzle problem implementation
│   ├── queens8/         # 8-queens problem implementation
│   └── run_experiments.py
├── data/               # Experimental results in CSV format
├── figures/            # Generated plots and visualizations
├── docs/              # Reference materials and documentation
└── report/            # Final report in IEEE format
```

## Setup Instructions

1. **Environment Requirements**
   - Python 3.8 or higher
   - Required packages listed in `requirements.txt`

2. **Installation**
   ```bash
   pip install -r requirements.txt
   ```

3. **Running Experiments**
   ```bash
   # Run full experiments
   python -m src.run_experiments
   
   # Run test with fewer instances
   python -m src.test_run
   ```

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