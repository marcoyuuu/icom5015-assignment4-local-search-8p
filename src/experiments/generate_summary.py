import pandas as pd
import numpy as np
from pathlib import Path

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(parents=True, exist_ok=True)

# Read the experiment results
results_file = data_dir / 'experiment_results.csv'
if not results_file.exists():
    print("No experiment results found. Please run the experiments first.")
    exit(1)

df = pd.read_csv(results_file)

# Calculate summary statistics
summary = df.groupby(['Algorithm', 'Problem']).agg({
    'Solution Found': ['mean', lambda x: x.mean() * 100],  # Convert to percentage
    'Steps': ['mean', 'std'],
    'Runtime': ['mean', 'std'],
    'Value Improvement': ['mean', 'std']
}).round(2)

# Rename columns
summary.columns = ['Solution Rate', 'Success %', 'Avg Steps', 'Steps Std', 'Avg Time', 'Time Std', 'Avg Improvement', 'Improvement Std']

# Save summary to CSV
summary.to_csv(data_dir / 'results_summary.csv')

print("Generated results summary in data/results_summary.csv") 