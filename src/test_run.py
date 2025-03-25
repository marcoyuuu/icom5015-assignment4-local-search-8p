from .run_experiments import run_8puzzle_experiments, run_8queens_experiments, plot_results
from pathlib import Path
import pandas as pd

def main():
    # Set up directories
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    figures_dir = base_dir / 'figures'
    
    # Run experiments with fewer instances
    print("Running 8-puzzle experiments (5 instances)...")
    puzzle_results = run_8puzzle_experiments(num_instances=5)
    
    print("Running 8-queens experiments (5 instances)...")
    queens_results = run_8queens_experiments(num_instances=5)
    
    # Combine results
    all_results = pd.concat([puzzle_results, queens_results], ignore_index=True)
    
    # Save raw results
    data_dir.mkdir(parents=True, exist_ok=True)
    all_results.to_csv(data_dir / 'test_results.csv', index=False)
    
    # Create visualizations
    print("Generating plots...")
    plot_results(all_results, figures_dir)
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("------------------")
    success_rates = all_results.groupby(['Problem', 'Algorithm'])['Solution Found'].mean() * 100
    print("\nSuccess Rates (%):")
    print(success_rates)
    
    avg_steps = all_results.groupby(['Problem', 'Algorithm'])['Steps'].mean()
    print("\nAverage Steps:")
    print(avg_steps)
    
    avg_runtime = all_results.groupby(['Problem', 'Algorithm'])['Runtime'].mean()
    print("\nAverage Runtime (seconds):")
    print(avg_runtime)
    
    print("\nTest completed. Results saved to data/test_results.csv and figures/")

if __name__ == "__main__":
    main() 