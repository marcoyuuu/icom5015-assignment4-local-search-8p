# Algorithm Documentation

## Local Search Algorithms Overview

Local search algorithms are optimization techniques that work by making incremental improvements to a current solution. They are particularly useful for problems where the path to the solution is less important than the solution itself.

### Common Characteristics
- Work with complete states rather than partial assignments
- Generally use an evaluation function to guide the search
- Can get stuck in local optima
- Often more memory-efficient than systematic search algorithms

## Implemented Algorithms

### 1. Hill Climbing

#### Steepest Ascent Hill Climbing
```python
def hill_climbing_steepest(initial_state, get_neighbors, evaluate):
    current = initial_state
    while True:
        neighbors = get_neighbors(current)
        best_neighbor = max(neighbors, key=evaluate)
        if evaluate(best_neighbor) <= evaluate(current):
            return current
        current = best_neighbor
```

**Characteristics:**
- Always moves to the best neighboring state
- Complete neighborhood evaluation
- Guaranteed to reach local optimum
- Can get stuck in:
  - Local maxima
  - Plateaus
  - Ridges

#### First-Choice Hill Climbing
```python
def hill_climbing_first_choice(initial_state, get_neighbors, evaluate):
    current = initial_state
    while True:
        found_better = False
        neighbors = get_neighbors(current)
        random.shuffle(neighbors)
        
        for neighbor in neighbors:
            if evaluate(neighbor) > evaluate(current):
                current = neighbor
                found_better = True
                break
                
        if not found_better:
            return current
```

**Characteristics:**
- Accepts first improving neighbor
- More efficient in large state spaces
- Can escape some local maxima through randomization
- Generally faster than steepest ascent

#### Random-Restart Hill Climbing
```python
def hill_climbing_random_restart(initial_state, get_neighbors, evaluate, 
                               generate_state, max_restarts=10):
    best_state = initial_state
    best_value = evaluate(initial_state)
    
    for _ in range(max_restarts):
        current = generate_state()
        result = hill_climbing_steepest(current, get_neighbors, evaluate)
        if evaluate(result) > best_value:
            best_state = result
            best_value = evaluate(result)
            
    return best_state
```

**Characteristics:**
- Multiple random starting points
- Can escape local maxima
- Higher computational cost
- Better solution quality on average

### 2. Simulated Annealing

```python
def simulated_annealing(initial_state, get_neighbors, evaluate, schedule):
    current = initial_state
    t = 1.0
    
    while t > 0:
        T = schedule(t)
        if T == 0:
            return current
            
        neighbor = random.choice(get_neighbors(current))
        delta_E = evaluate(neighbor) - evaluate(current)
        
        if delta_E > 0 or random.random() < math.exp(delta_E / T):
            current = neighbor
            
        t += 1
```

#### Cooling Schedules

1. **Exponential Schedule**
```python
def exponential_schedule(k=20, lam=0.005):
    return lambda t: k * math.exp(-lam * t)
```

2. **Linear Schedule**
```python
def linear_schedule(k=100):
    return lambda t: max(0, k - t)
```

**Characteristics:**
- Probabilistic acceptance of worse states
- Can escape local maxima
- Convergence depends on cooling schedule
- Better at avoiding local optima than hill climbing

## Problem-Specific Implementations

### 8-Puzzle Problem

#### State Representation
- List of 9 integers (0-8)
- 0 represents empty space
- Goal state: [1, 2, 3, 4, 5, 6, 7, 8, 0]

#### Evaluation Function
```python
def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            curr_row, curr_col = i // 3, i % 3
            goal_row, goal_col = state[i] // 3, state[i] % 3
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return -distance  # Negated for maximization
```

### 8-Queens Problem

#### State Representation
- List of 8 integers (0-7)
- Each number represents queen's column position in corresponding row
- Goal: No queens threatening each other

#### Evaluation Function
```python
def count_conflicts(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j]:  # Same column
                conflicts += 1
            if abs(state[i] - state[j]) == j - i:  # Diagonal
                conflicts += 1
    return -conflicts  # Negated for maximization
```

## Algorithm Selection Guidelines

1. **Use Hill Climbing when:**
   - Quick solution needed
   - Problem has many acceptable solutions
   - Memory is limited
   - Local optima are acceptable

2. **Use Random-Restart Hill Climbing when:**
   - Better solution quality needed
   - Computational time available
   - Multiple runs possible

3. **Use Simulated Annealing when:**
   - Global optimum desired
   - Gradual improvement acceptable
   - Problem has many local optima
   - Complex state space topology

## Performance Considerations

### Time Complexity
- Hill Climbing: O(bd) where b is branching factor, d is depth
- Random-Restart: O(n * bd) where n is number of restarts
- Simulated Annealing: O(t * b) where t is number of iterations

### Space Complexity
- All algorithms: O(b) where b is branching factor
- Only need to store current state and neighbors

### Trade-offs
- Solution Quality vs. Computation Time
- Exploration vs. Exploitation
- Memory Usage vs. Performance 