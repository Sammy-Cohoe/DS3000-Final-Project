"""
DS3000 Final Project - Phase 1: Data Loading and Exploration

This is the main script that orchestrates the data analysis workflow.
"""

from src.data.data_loader import load_data, get_basic_info
from src.visualization.exploratory_analysis import exploratory_plots

def main():
    print("=" * 60)
    print("DS3000 Final Project - Phase 1")
    print("CO2 Emissions Canada Dataset Analysis")
    print("=" * 60)

    # Step 1: Load data
    print("\n[Step 1] Loading data...")
    data = load_data()

    # Step 2: Get basic information
    print("\n[Step 2] Exploring dataset...")
    get_basic_info(data)

    # Step 3: Generate exploratory visualizations
    print("\n[Step 3] Creating visualizations...")
    exploratory_plots(data)

    print("\n" + "=" * 60)
    print("Phase 1 Complete!")
    print("Check outputs/figures/ for generated visualizations")
    print("=" * 60)

if __name__ == "__main__":
    main()
