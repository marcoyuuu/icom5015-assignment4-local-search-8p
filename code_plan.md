### High-Level Integration & Code Development Plan

#### 1. **Project Directory Structure**
- **src/berkeley_ai/**  
  - Contains: `search.py`, `utils.py`  
  - Provides A* search, local search algorithms, heuristic functions, and general search framework.
- **src/8queens/**  
  - Integrate code from [M-S-Saurabh](https://github.com/M-S-Saurabh/8-Queens-Puzzle) and [N. Shahabi](https://github.com/nikashahabi/8queen-problem-solve-with-hill-climbing-and-simulated-annealing) for 8-Queens implementations.
- **src/8puzzle/**  
  - Develop functions to generate and validate random 8-puzzle instances.
- **data/**  
  - Store generated experiment results (CSV/JSON).
- **figures/**  
  - Store plots, graphs, and charts.
- **report/**  
  - Contains the final report document (formatted per IEEE guidelines).

---

#### 2. **Environment Setup**
- Ensure Python is installed (version 3.8+ recommended).
- Install necessary libraries (NumPy, Pandas, Matplotlib, Jupyter Notebook).
- Add the `src/berkeley_ai/` directory to the Python path so that modules in `search.py` and `utils.py` are importable.

---

### 📁 **Resources Directory**

To implement this project, make use of the local resources and references available at:

```
Directory: C:\Users\Marco\Uni\AI\Assignments\A4\AI_LocalSearch_8P\docs
```

The following files contain valuable implementation details, algorithm examples, and theoretical explanations. These must be parsed and used where appropriate:

| File Name                                                            | Description                                                                                  |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| `m-s-saurabh-8-queens-puzzle.txt`                                    | Contains implementation examples for 8-Queens using local search techniques.                |
| `nikashahabi-8queen-problem-solve-with-hill-climbing-and-simulated-annealing.txt` | Contains both hill climbing and simulated annealing examples for the 8-Queens problem.      |
| `newchap04.txt`                                                      | Text version of Chapter 4 from the *AIMA* book. Use this to justify algorithmic choices and cite theory. |
| `Yale Search Algorithms.txt`                                         | Supplementary notes from Yale’s CS470 course. Reference to strengthen understanding of search dynamics. |

✅ **Action for Agent:**  
Ensure that code logic, explanations, and analysis align with these files. Reuse snippets or adapt functions as needed, and cite in the final report when referencing logic derived from these documents.

---

#### 3. **Integrating Core Search Functions from AIMA Repository**
- **Importing Code:**  
  In your main implementation script or notebook, import the AIMA modules as follows:
  ```python
  from src.berkeley_ai.search import *      # All search functions and classes
  from src.berkeley_ai.utils import *       # Utility functions (e.g., memoize, PriorityQueue)
  ```
- **Leverage Existing Algorithms:**  
  Use the provided A* implementation as a baseline to compute optimal solution costs for the 8-puzzle instances.  
  Also, reuse parts of the local search framework (like hill climbing and simulated annealing) from the AIMA code if available or build on it.

---

#### 4. **Developing Problem Instance Generators**
- **8-Puzzle Generator:**  
  - Write a function `generate_8puzzle_instance()` that produces a random, solvable 8-puzzle configuration.
  - Validate the generated instance using established methods (e.g., inversion count).
- **8-Queens Generator:**  
  - Write a function `generate_8queens_state()` that randomly assigns one queen per column (a complete state).
  - Optionally integrate code from the 8-Queens GitHub projects to validate and measure heuristics.

---

#### 5. **Implementing Local Search Algorithms**
- **Hill Climbing (Steepest-Ascent & First-Choice):**  
  - Create wrappers for both variants.
  - Use the state representation from the 8-Queens generator.
  - Optionally, integrate code snippets from [M-S-Saurabh] and [N. Shahabi] repositories.
- **Random Restart Hill Climbing:**  
  - Build a loop that generates new random states and runs hill climbing until a solution is found.
- **Simulated Annealing:**  
  - Implement a cooling schedule (e.g., exponential decay) within your simulated annealing function.
  - Leverage or adapt the simulated annealing code available in the external GitHub repositories if it fits the requirements.

---

#### 6. **Metrics Collection & Experiment Control**
- **Metrics to Collect:**  
  - Number of moves/steps taken per instance.
  - Whether the solution was found (and for 8-puzzle, how it compares to the optimal cost computed via A*).
  - Runtime for each algorithm.
- **Experiment Script:**  
  - Create an experiment driver script (`run_experiments.py`) that:
    1. Iterates over a predefined number of problem instances.
    2. Runs each algorithm variant (steepest-ascent, first-choice, random restart, simulated annealing) on both 8-puzzle and 8-queens.
    3. Logs the metrics in a structured format (using Pandas DataFrames or writing CSV/JSON files).
    4. Updates a progress indicator for long experiments.
  
  Example pseudocode:
  ```python
  for instance in range(NUM_INSTANCES):
      puzzle_instance = generate_8puzzle_instance()
      queens_instance = generate_8queens_state()
      
      # Run and record metrics for each algorithm:
      optimal_cost = astar_search(puzzle_instance).cost
      
      hc_solution, hc_moves = hill_climbing_steepest(puzzle_instance)
      fc_solution, fc_moves = hill_climbing_first_choice(puzzle_instance)
      rr_solution, rr_moves = hill_climbing_random_restart(puzzle_instance)
      sa_solution, sa_moves = simulated_annealing(puzzle_instance)
      
      # Record for 8-queens similarly
      
      # Append results to DataFrame
      update_results(...)
  ```
  
---

#### 7. **Data Visualization & Reporting**
- **Plotting:**  
  - Use Matplotlib to create:
    - Bar charts comparing success rate (%) of each algorithm.
    - Line graphs of average moves versus optimal cost.
    - Scatter plots for runtime comparisons.
- **Export Figures:**  
  Save figures to the `figures/` directory.
- **Report Generation:**  
  - Compile a report in the `report/` folder with your experimental setup, results (tables/figures), and analysis.
  - Include IEEE citations for all external resources ([1]–[7]).

---

#### 8. **Instructions to Cursor AI**
Provide the following summary to Cursor AI as instructions for the code development:
> "Develop a complete project for solving 8-puzzle and 8-queens problems using local search algorithms (hill climbing variants, random restart hill climbing, and simulated annealing). Integrate AIMA search functions from `src/berkeley_ai/search.py` and `src/berkeley_ai/utils.py`. Build generators for problem instances, implement experiment drivers that run multiple instances, collect and log metrics (moves, success rate, runtime), and create visualizations (bar charts, line graphs). Finally, generate a report that includes IEEE citations and a discussion of results."

---

### Final Notes
This plan outlines both the integration of the AIMA repository code and how to incorporate additional resources. Use it to instruct Cursor AI to develop the full implementation pipeline, from instance generation and algorithm execution to data collection and reporting.
