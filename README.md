# DS3000 Final Project - CO2 Emissions Analysis

Analysis of CO2 emissions data from Canada.

## Project Structure

```
DS3000-Final-Project/
│
├── data/
│   ├── raw/                    # Original, immutable data
│   │   └── CO2_Emissions_Canada.csv
│   └── processed/              # Cleaned, processed data
│
├── notebooks/                  # Jupyter notebooks for exploration
│   └── Final_Project.py        # Original exploratory script
│
├── src/                        # Source code for use in this project
│   ├── data/                   # Scripts to load and process data
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── preprocessing.py
│   │
│   ├── visualization/          # Scripts for visualizations
│   │   ├── __init__.py
│   │   └── exploratory_analysis.py
│   │
│   └── models/                 # Scripts for model training
│       └── __init__.py
│
├── outputs/                    # Generated analysis outputs
│   ├── figures/                # Generated graphics and figures
│   └── models/                 # Trained model files
│
├── main.py                     # Main script to run the analysis
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main analysis:
```bash
python main.py
```

This will:
- Load the CO2 emissions dataset
- Display basic statistics and information
- Generate visualizations in `outputs/figures/`
