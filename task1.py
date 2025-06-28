import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.optimize import minimize

# Load and clean data
df = pd.read_csv("auto-mpg.csv")
df = df.replace("?", np.nan)
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df = df.dropna().reset_index(drop=True)

# Normalize
features = ['mpg', 'horsepower', 'weight']
scaler = MinMaxScaler()
X = scaler.fit_transform(df[features])

# Define objective function (negate mpg and horsepower to maximize them)
def objective(x):
    mpg = x[0]
    horsepower = x[1]
    weight = x[2]
    
    # Weighted sum: maximize mpg & horsepower, minimize weight
    return -0.4 * mpg - 0.4 * horsepower + 0.2 * weight

# Initial guess
x0 = np.mean(X, axis=0)

# Bounds between 0 and 1 (normalized)
bounds = [(0, 1), (0, 1), (0, 1)]

# Minimize the single objective
result = minimize(objective, x0, bounds=bounds)

# Print result
print("Optimized result (normalized):", result.x)
print("Optimized objective score:", result.fun)
