import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

data = pd.read_csv('CO2_Emissions_Canada.csv')

print(data.head())
print(data.describe())

data.hist(figsize=(12, 8), bins=20)
plt.tight_layout()
plt.show()
