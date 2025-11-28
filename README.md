# DS3000 Final Project - CO2 Emissions Analysis

**Objective**: Predict CO₂ emissions from vehicle characteristics using machine learning to inform policy decisions and guide consumers toward eco-friendly vehicles.

## Project Structure

```
DS3000-Final-Project/
│
├── data/
│   ├── raw/                          # Original, immutable data
│   │   └── CO2_Emissions_Canada.csv
│   └── processed/                    # Cleaned, processed data
│       └── CO2_processed.csv         # Feature-engineered dataset
│
├── notebooks/                        # Jupyter notebooks for exploration
│   └── Final_Project.py              # Original exploratory script
│
├── src/                              # Source code modules
│   ├── data/                         # Data processing
│   │   ├── __init__.py
│   │   ├── data_loader.py            # Load and inspect data
│   │   └── preprocessing.py          # Feature engineering & encoding
│   │
│   ├── visualization/                # Visualization functions
│   │   ├── __init__.py
│   │   └── exploratory_analysis.py   # Plots and correlation analysis
│   │
│   └── models/                       # Model training (Phase 2)
│       └── __init__.py
│
├── outputs/                          # Generated outputs
│   ├── figures/                      # Visualizations
│   │   ├── distributions.png
│   │   ├── correlation_heatmap.png
│   │   ├── feature_correlations.png
│   │   └── top_features_scatter.png
│   └── models/                       # Saved models
│
├── main.py                           # Phase 0 script
├── phase1.py                         # Phase 1 script
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Phase 1: Data Loading & Exploratory Analysis
```bash
python main.py
```

This will:
- Load the CO2 emissions dataset (7,385 vehicle records)
- Display dataset statistics and information
- Generate distribution histograms
- Create correlation heatmap

**Outputs**: `outputs/figures/distributions.png`, `outputs/figures/correlation_heatmap.png`

### Phase 2: Feature Engineering & Analysis
```bash
python phase2.py
```

This will:
- Check for missing values
- Create 3 derived features:
  - `Power_Efficiency` - Cylinders per liter
  - `Fuel_Diff` - City vs highway fuel consumption difference
  - `Displacement_Per_Cyl` - Engine size per cylinder
- One-hot encode Fuel Type and Vehicle Class
- Analyze feature correlations with CO₂ emissions
- Generate feature importance visualizations

**Outputs**:
- `data/processed/CO2_processed.csv` - Processed dataset
- `outputs/figures/feature_correlations.png` - Top 10 correlations
- `outputs/figures/top_features_scatter.png` - Scatter plots
- `outputs/feature_correlations.csv` - Full correlation results

**Documentation**: See [PHASE2_ANALYSIS.md](PHASE2_ANALYSIS.md) for detailed methodology

### Phase 3: Model Building (Coming Soon)
- Train multiple regression models
- Compare model performance
- Extract feature importance
- Generate predictions

## Project Phases

- ✅ **Phase 1**: Data loading and exploratory analysis
- ✅ **Phase 2**: Feature engineering and correlation analysis
- 🔄 **Phase 3**: Model training, evaluation, and interpretation

## Key Features

- **Clean Architecture**: Modular code structure following data science best practices
- **Reproducible**: Fixed random seeds and clear documentation
- **Scalable**: Easy to add new features or models
- **Well-Documented**: Inline comments and methodology reports

## Dataset

**CO2 Emissions Canada** - 7,385 vehicle records with 12 original features:
- Make, Model, Vehicle Class
- Engine Size, Cylinders, Transmission
- Fuel Type
- Fuel Consumption (City, Highway, Combined)
- **Target**: CO2 Emissions (g/km)
