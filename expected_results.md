### ✅ **Expected Results Overview**

---

#### 🔹 **1. Success Rate (Solvability)**
- **Definition:** Percentage of problem instances successfully solved (i.e., reached a goal state) by each algorithm.
- **Expectation:**
  - **Simulated Annealing** tends to solve **more** 8-queens instances than standard Hill Climbing (due to escape from local maxima).
  - **Random Restart Hill Climbing** will improve success rate significantly over plain Steepest-Ascent or First-Choice.

---

#### 🔹 **2. Search Cost / Number of Steps**
- **Definition:** Number of state transitions (moves) taken until the solution is found or failure is reported.
- **Expectation:**
  - **Simulated Annealing** may take more steps but finds better solutions more consistently.
  - **First-Choice Hill Climbing** generally explores fewer neighbors per step → faster but less reliable.

---

#### 🔹 **3. Time Taken**
- **Definition:** Average CPU time (or wall-clock time) to solve each instance.
- **Expectation:**
  - Hill climbing is faster per instance.
  - Simulated annealing might be slower due to stochastic exploration and cooling schedules.

---

#### 🔹 **4. Optimality (for 8-Puzzle Only)**
- **Definition:** Compare the cost (steps) of the local search solution to the **optimal cost** found using A* (from `search.py`).
- **Expectation:**
  - Hill climbing will often find sub-optimal solutions (i.e., longer paths).
  - A* sets a lower bound for each instance’s solution cost.

---

#### 🔹 **5. Visual and Statistical Results**
- You are expected to **produce the following plots**:
  - **Bar Chart** or **Line Graph**: Search cost vs. algorithm
  - **Success Rate Histogram**: Percentage of solved instances
  - **Scatter Plot**: Search cost vs. optimal cost (for 8-puzzle)
  - **Box Plot or Distribution Plot**: Variation in steps taken per algorithm

---

### 📈 **Summary Table Example**

| Algorithm                   | Avg. Steps | Success Rate | Avg. Time (ms) | Optimality (8-Puzzle) |
|----------------------------|------------|---------------|----------------|------------------------|
| Steepest-Ascent Hill Climb | 14.7       | 42%           | 1.5            | Low                    |
| First-Choice Hill Climb    | 10.3       | 55%           | 1.2            | Moderate               |
| Random-Restart Hill Climb  | 8.9        | 95%           | 3.2            | Moderate–High          |
| Simulated Annealing        | 9.8        | 98%           | 5.4            | High                   |
| A* (reference only)        | 7.0        | 100%          | 8.7            | Optimal                |

---

### 📄 **Report Expectations (from class and PDF guide)**
You are expected to:
- Present **quantitative** comparison (in tables/figures).
- Interpret and **comment on trade-offs**: e.g., why faster doesn’t mean better.
- Justify algorithm behavior using theory from:
  - AIMA Chapter 4【1】
  - Berkeley/Yale materials【2】【3】【7】
- Cite and refer to implementations if inspired by GitHub repos【5】【6】
