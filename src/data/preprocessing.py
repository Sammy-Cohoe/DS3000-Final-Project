from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd


def check_missing_values(data):
    """Check for missing values in the dataset"""
    missing = data.isnull().sum()
    if missing.sum() == 0:
        print("✓ No missing values found!")
    else:
        print("Missing values:")
        print(missing[missing > 0])
    return missing


def create_derived_features(data):
    """Create new features from existing ones"""
    data = data.copy()

    # Power efficiency (cylinders per liter)
    data['Power_Efficiency'] = data['Cylinders'] / data['Engine Size(L)']

    # Fuel consumption difference (city vs highway)
    data['Fuel_Diff'] = data['Fuel Consumption City (L/100 km)'] - \
                        data['Fuel Consumption Hwy (L/100 km)']

    # Engine displacement per cylinder
    data['Displacement_Per_Cyl'] = data['Engine Size(L)'] / data['Cylinders']

    print("✓ Created 3 derived features")
    return data


def encode_features(data):
    """Encode categorical features"""
    data = data.copy()

    # One-hot encode Fuel Type
    data = pd.get_dummies(data, columns=['Fuel Type'], prefix='Fuel', drop_first=True)

    # One-hot encode Vehicle Class
    data = pd.get_dummies(data, columns=['Vehicle Class'], prefix='Class', drop_first=True)

    # Drop high-cardinality categorical columns
    data = data.drop(columns=['Make', 'Model', 'Transmission'])

    print(f"✓ Encoded features. New shape: {data.shape}")
    return data


def prepare_data(data, target_column, test_size=0.2, random_state=42):
    """Split data into train/test sets and separate features from target"""
    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    print(f"✓ Training set: {len(X_train)} samples")
    print(f"✓ Test set: {len(X_test)} samples")

    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """Standardize features using StandardScaler"""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("✓ Features scaled")
    return X_train_scaled, X_test_scaled, scaler
