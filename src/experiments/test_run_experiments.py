import unittest
from pathlib import Path
import pandas as pd
from run_experiments import (
    calculate_summary_statistics,
    generate_summary,
    generate_puzzle_results,
    generate_queens_results
)

class TestRunExperiments(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.data_dir = Path('data')
        self.data_dir.mkdir(exist_ok=True)
        
        # Create sample data for testing
        self.sample_data = pd.DataFrame({
            'Problem': ['8-Puzzle', '8-Puzzle', '8-Queens', '8-Queens'],
            'Algorithm': ['Hill Climbing', 'Simulated Annealing', 'Hill Climbing', 'Simulated Annealing'],
            'Solution Found': [0.8, 0.9, 0.7, 0.85],
            'Steps': [100, 120, 80, 90],
            'Runtime': [0.5, 0.6, 0.4, 0.45],
            'Value Improvement': [0.3, 0.4, 0.25, 0.35]
        })

    def test_calculate_summary_statistics(self):
        """Test the calculation of summary statistics for plotting."""
        summary = calculate_summary_statistics(self.sample_data)
        
        # Check if all required columns are present
        required_columns = ['Solution Rate', 'Success %', 'Avg Steps', 'Steps Std', 'Avg Time', 'Time Std']
        for col in required_columns:
            self.assertIn(col, summary.columns)
        
        # Check if statistics are calculated correctly
        self.assertEqual(len(summary), 4)  # 2 problems * 2 algorithms
        self.assertTrue(all(summary['Success %'] >= 0 and summary['Success %'] <= 100))

    def test_generate_summary(self):
        """Test the generation and saving of summary statistics."""
        generate_summary(self.sample_data, self.data_dir)
        
        # Check if summary file was created
        summary_file = self.data_dir / 'results_summary.csv'
        self.assertTrue(summary_file.exists())
        
        # Check if summary file contains correct data
        summary = pd.read_csv(summary_file)
        required_columns = ['Solution Rate', 'Success %', 'Avg Steps', 'Steps Std', 'Avg Time', 'Time Std', 'Avg Improvement', 'Improvement Std']
        for col in required_columns:
            self.assertIn(col, summary.columns)

    def test_generate_puzzle_results(self):
        """Test the generation of 8-puzzle results."""
        results = generate_puzzle_results()
        
        # Check if results DataFrame has required columns
        required_columns = ['Problem', 'Algorithm', 'Solution Found', 'Steps', 'Runtime', 'Value Improvement']
        for col in required_columns:
            self.assertIn(col, results.columns)
        
        # Check if all algorithms are included
        algorithms = results['Algorithm'].unique()
        self.assertIn('Hill Climbing', algorithms)
        self.assertIn('Simulated Annealing', algorithms)

    def test_generate_queens_results(self):
        """Test the generation of 8-queens results."""
        results = generate_queens_results()
        
        # Check if results DataFrame has required columns
        required_columns = ['Problem', 'Algorithm', 'Solution Found', 'Steps', 'Runtime', 'Value Improvement']
        for col in required_columns:
            self.assertIn(col, results.columns)
        
        # Check if all algorithms are included
        algorithms = results['Algorithm'].unique()
        self.assertIn('Hill Climbing', algorithms)
        self.assertIn('Simulated Annealing', algorithms)

    def tearDown(self):
        """Clean up test environment."""
        # Remove test files
        summary_file = self.data_dir / 'results_summary.csv'
        if summary_file.exists():
            summary_file.unlink()

if __name__ == '__main__':
    unittest.main() 