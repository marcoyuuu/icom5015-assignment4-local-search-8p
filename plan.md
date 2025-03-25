### 1. **Assignment Overview & Objectives**

- **Task:**  
  Generate many instances of the 8-puzzle and 8-queens problems. Solve them using various local search algorithms:  
  - Hill Climbing (both steepest-ascent and first-choice variants)  
  - Hill Climbing with Random Restart  
  - Simulated Annealing

- **Metrics to Measure:**  
  - Search cost (e.g., number of moves or nodes expanded)  
  - Percentage of solved problems  
  - Comparison of these metrics against the optimal solution cost (for example, using A* for the 8-puzzle)

- **Deliverables:**  
  A formal report that includes tables and graphs comparing algorithm performance and a critical analysis of the results. The report must follow IEEE citation guidelines and the presentation format described by [7].

---

### 2. **Resources & References**

- **Textbook Chapter:**  
  *Russell and Norvig, “Chapter 4: Beyond Classical Search”* ([1]). Use this chapter to understand informed search and the theoretical basis for the algorithms.

- **Python Implementation (aima-python):**  
  The UC Berkeley AI project repository ([2]) provides a solid base for many search algorithms. This is especially useful for setting up A* (for optimal solution cost) and other search variants.

- **Yale Search Algorithms:**  
  The Yale University resource ([3]) offers additional visualizations and explanations of search algorithms, reinforcing your understanding of informed and local search strategies.

- **YouTube Tutorial:**  
  Ayushi Bainalwar’s video ([4]) explains solving the 8-queens problem using local search, which can help clarify implementation details and algorithm behavior.

- **8-Queens Code Repositories:**  
  Two GitHub projects – one by M. S. Saurabh ([5]) and one by N. Shahabi ([6]) – include implementations of hill climbing and simulated annealing for the 8-queens problem. They provide ready-to-use code and insights into performance metrics.

- **Class Presentation:**  
  The class presentation by Dr. José Fernando Vega-Riveros ([7]) gives a clear, visual, and intuitive overview of heuristic search, hill climbing, simulated annealing, and genetic algorithms. Use these slides to explain the conceptual foundations and challenges (e.g., local minima, plateaux) in your report.

---

### 3. **Project Organization & Folder Structure**

- **Folder Name:**  
  Use a concise folder name, for example, `AI_LocalSearch_8P`.

- **Structure:**
  - `AI_LocalSearch_8P/`
    - `code/` – all your Python scripts and Jupyter notebooks.
    - `data/` – CSV or JSON files for experimental results.
    - `figures/` – graphs and charts generated from the experiments.
    - `report/` – your formal report document following IEEE style.

---

### 4. **Implementation Plan**

#### A. **Environment Setup**
- Install Python, Jupyter Notebook, and required libraries (e.g., NumPy, Pandas, matplotlib).
- Clone the `aima-python` repository ([2]) and any code from [5] and [6] for the 8-queens part.
- Set a reproducible random seed for consistent results.

#### B. **Generating Problem Instances**
- **8-Puzzle:**  
  - Write a function to generate random but solvable 8-puzzle instances.
  - Use A* (from aima-python) to compute the optimal cost for each instance.

- **8-Queens:**  
  - Write a generator that produces random complete states (one queen per column).
  - Verify if the state is a solution (heuristic value = 0) for the 8-queens problem.

#### C. **Algorithm Integration & Experimentation**
- **Implement and Test Local Search Variants:**
  - **Hill Climbing (Steepest-Ascent):** Use the implementation from [5] or [6] as a base.
  - **Hill Climbing (First-Choice):** Similarly, integrate the first-choice variant.
  - **Random Restart Hill Climbing:** Create a loop that reinitializes the search if a local minimum is encountered.
  - **Simulated Annealing:** Use provided code from [6] or adapt from [1] examples.

- **Metrics Collection:**
  - For each algorithm and each instance, record:
    - Number of moves (or steps)
    - Whether a solution was found (and, if so, if it is optimal for 8-puzzle)
  - Store these metrics in a DataFrame or CSV file.

#### D. **Data Analysis & Visualization**
- **Graphing:**
  - Plot the search cost (average number of moves) versus the optimal cost (for 8-puzzle).
  - Plot the percentage of solved instances for each algorithm.
  - Create tables summarizing performance for both problem types.

- **Analysis:**
  - Discuss why some algorithms perform better (e.g., random restarts improve hill climbing in 8-queens).
  - Compare efficiency differences between 8-puzzle and 8-queens.
  - Relate observations to the theoretical insights from [1] and the class presentation ([7]).

---

### 5. **Report Writing**

- **Structure:**  
  - **Title Page:** Include course info and project title.
  - **Abstract:** Summarize objectives, methods, and key findings.
  - **Introduction:** Provide background, problem statement, and significance.
  - **Methodology:**  
    - Describe problem instance generation (8-puzzle and 8-queens).
    - Detail the algorithms used and why they were chosen.
    - Explain how metrics were collected.
  - **Results:**  
    - Include tables and figures with captions (e.g., "Table 1 – Average Search Cost vs. Optimal Cost").
    - Compare algorithm performance.
  - **Analysis & Discussion:**  
    - Interpret the results.
    - Discuss advantages and limitations.
  - **Conclusion:** Summarize findings and potential improvements.
  - **References:**  
    - List all IEEE-style citations ([1] through [7]) as provided.
  
- **IEEE Style:**  
  - Follow the provided IEEE citation guidelines when referencing each resource.
  - Use clear, concise language and proper formatting for tables and figures.

---

### 6. **Final Steps & Quality Assurance**

- **Testing:**  
  - Run the complete suite of experiments multiple times to verify consistency.
  - Validate the correctness of both the 8-puzzle and 8-queens solutions.

- **Review & Revision:**  
  - Revise your code for efficiency and readability.
  - Peer review the report content to ensure clarity and adherence to guidelines.
  - Double-check citations and references for accuracy.

- **Submission:**  
  - Package the code folder, data, figures, and report into a compressed archive.
  - Ensure the README (or documentation) explains how to run the experiments.

---

### Conclusion

By following this comprehensive plan, you will leverage theoretical insights ([1]), practical implementations ([2], [5], [6]), and class presentation content ([7])—along with additional resources from Yale ([3]) and YouTube ([4])—to build a robust experimental study. Your final report will not only demonstrate the performance of various local search algorithms on 8-puzzle and 8-queens instances but also provide a detailed analysis backed by both theoretical and experimental evidence.
