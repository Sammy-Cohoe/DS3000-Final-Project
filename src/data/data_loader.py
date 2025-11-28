import pandas as pd

def load_data(filepath='data/raw/CO2_Emissions_Canada.csv'):
    # Load the CO2 emissions dataset
    data = pd.read_csv(filepath)
    return data

def get_basic_info(data):
    # Display basic information about the dataset
    print("Dataset Shape:", data.shape)
    print("\nFirst few rows:")
    print(data.head())
    print("\nDataset Info:")
    print(data.info())
    print("\nBasic Statistics:")
    print(data.describe())
    print("\nMissing Values:")
    print(data.isnull().sum())
    return data
