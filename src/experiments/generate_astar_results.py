from ..search.astar_search import PuzzleState, astar_search, generate_solvable_puzzle
import pandas as pd
import time

# Generate results for 100 random instances
results = []
n_instances = 100

for i in range(n_instances):
    # Generate a solvable puzzle
    puzzle = generate_solvable_puzzle()
    state = PuzzleState(puzzle)
    
    # Get A* solution
    start_time = time.time()
    solution = astar_search(state)
    end_time = time.time()
    
    result = {
        'Instance': i,
        'Initial_State': str(puzzle),
        'Steps': len(solution.path()) if solution else 0,
        'Runtime': end_time - start_time,
        'Solved': solution is not None
    }
    results.append(result)
    print(f"Instance {i}: {'Solved' if solution else 'Unsolved'} in {result['Steps']} steps")

# Convert to DataFrame and save
df = pd.DataFrame(results)
df.to_csv('data/astar_results.csv', index=False)
print(f"\nGenerated A* results for {n_instances} instances")
print(f"Average steps for solved instances: {df[df['Solved']]['Steps'].mean():.1f}")
print(f"Average runtime: {df['Runtime'].mean():.3f} seconds") 