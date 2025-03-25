from .run_experiments import run_8puzzle_experiments, run_8queens_experiments, plot_results
from pathlib import Path
import pandas as pd

def main():
    try:
        # Set up directories
        base_dir = Path(__file__).parent.parent
        data_dir = base_dir / 'data'
        figures_dir = base_dir / 'figures'
        
        # Create directories if they don't exist
        data_dir.mkdir(parents=True, exist_ok=True)
        figures_dir.mkdir(parents=True, exist_ok=True)
        
        # Run experiments with more instances
        print("Running 8-puzzle experiments...")
        try:
            puzzle_results = run_8puzzle_experiments(num_instances=50)
            # Save intermediate results
            puzzle_results.to_csv(data_dir / 'puzzle_results.csv', index=False)
        except KeyboardInterrupt:
            print("\n8-puzzle experiments interrupted. Saving partial results...")
            if 'puzzle_results' in locals():
                puzzle_results.to_csv(data_dir / 'puzzle_results_partial.csv', index=False)
            return
        except Exception as e:
            print(f"\nError in 8-puzzle experiments: {str(e)}")
            return
        
        print("Running 8-queens experiments...")
        try:
            queens_results = run_8queens_experiments(num_instances=50)
            # Save intermediate results
            queens_results.to_csv(data_dir / 'queens_results.csv', index=False)
        except KeyboardInterrupt:
            print("\n8-queens experiments interrupted. Saving partial results...")
            if 'queens_results' in locals():
                queens_results.to_csv(data_dir / 'queens_results_partial.csv', index=False)
            return
        except Exception as e:
            print(f"\nError in 8-queens experiments: {str(e)}")
            return
        
        # Combine results
        all_results = pd.concat([puzzle_results, queens_results], ignore_index=True)
        
        # Save raw results
        all_results.to_csv(data_dir / 'experiment_results.csv', index=False)
        
        # Create visualizations
        print("Generating plots...")
        try:
            plot_results(all_results, figures_dir)
        except Exception as e:
            print(f"\nError generating plots: {str(e)}")
            return
        
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
        
        print("\nExperiments completed. Results saved to data/ and figures/ directories.")
        
    except KeyboardInterrupt:
        print("\nTest script interrupted by user. Exiting...")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        raise

if __name__ == "__main__":
    main() 