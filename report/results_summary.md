# Performance Analysis of Local Search Algorithms

## Overview

This report presents a comprehensive analysis of various local search algorithms applied to the 8-Puzzle and 8-Queens problems. The algorithms evaluated include:
- Hill Climbing (Steepest Ascent)
- Hill Climbing (First Choice)
- Hill Climbing (Random Restart)
- Simulated Annealing (Exponential Schedule)
- Simulated Annealing (Linear Schedule)

## Results Summary

### 8-Puzzle Problem

| Algorithm | Success Rate (%) | Average Steps | Average Time (s) |
|-----------|-----------------|---------------|------------------|
| Hill Climbing (Steepest) | 0.0 | 2.02 | 0.000057 |
| Hill Climbing (First Choice) | 0.0 | 2.02 | 0.000043 |
| Hill Climbing (Random Restart) | 4.0 | 27.40 | 0.000440 |
| Simulated Annealing (Exponential) | 0.0 | 970.56 | 0.003994 |
| Simulated Annealing (Linear) | 8.0 | 242.72 | 0.004037 |

### 8-Queens Problem

| Algorithm | Success Rate (%) | Average Steps | Average Time (s) |
|-----------|-----------------|---------------|------------------|
| Hill Climbing (Steepest) | 6.0 | 2.34 | 0.000832 |
| Hill Climbing (First Choice) | 0.0 | 2.80 | 0.000494 |
| Hill Climbing (Random Restart) | 64.0 | 32.22 | 0.008112 |
| Simulated Annealing (Exponential) | 0.0 | 960.12 | 0.016389 |
| Simulated Annealing (Linear) | 52.0 | 245.26 | 0.015597 |

## Key Findings

### 8-Puzzle Problem
1. **Success Rates**:
   - Linear Simulated Annealing achieved the highest success rate (8%)
   - Random Restart Hill Climbing showed moderate success (4%)
   - Basic hill climbing variants failed to find solutions

2. **Step Count**:
   - Basic hill climbing variants took minimal steps (2.02)
   - Random Restart took moderate steps (27.40)
   - Simulated Annealing took significantly more steps (242.72-970.56)

3. **Runtime**:
   - Basic hill climbing was fastest (0.000043-0.000057s)
   - Random Restart was moderately fast (0.000440s)
   - Simulated Annealing was slowest (0.003994-0.004037s)

### 8-Queens Problem
1. **Success Rates**:
   - Random Restart Hill Climbing achieved the highest success rate (64%)
   - Linear Simulated Annealing performed well (52%)
   - Steepest Ascent showed limited success (6%)

2. **Step Count**:
   - Basic hill climbing took minimal steps (2.34-2.80)
   - Random Restart took moderate steps (32.22)
   - Simulated Annealing took more steps (245.26-960.12)

3. **Runtime**:
   - Basic hill climbing was fastest (0.000494-0.000832s)
   - Random Restart was moderately fast (0.008112s)
   - Simulated Annealing was slowest (0.015597-0.016389s)

## Comparative Analysis

1. **Problem Difficulty**:
   - 8-Queens proved easier to solve than 8-Puzzle
   - Higher success rates across all algorithms for 8-Queens

2. **Algorithm Performance**:
   - Random Restart Hill Climbing consistently outperformed basic hill climbing
   - Linear cooling schedule performed better than exponential for Simulated Annealing
   - Basic hill climbing variants were fastest but least effective

3. **Trade-offs**:
   - Speed vs. Success: Faster algorithms had lower success rates
   - Steps vs. Success: More steps generally led to better success rates
   - Time vs. Quality: Longer runtimes correlated with better solutions

## Visualizations

The following visualizations are available in the `figures/` directory:
- Success rate comparisons
- Average step count analysis
- Runtime performance analysis
- Performance matrix heatmap
- Cross-problem comparisons

## Conclusions

1. Random Restart Hill Climbing provides the best balance of performance and efficiency for both problems
2. Linear cooling schedule for Simulated Annealing offers better results than exponential
3. Basic hill climbing variants are suitable only when speed is prioritized over solution quality
4. The 8-Queens problem is more amenable to local search approaches than the 8-Puzzle 