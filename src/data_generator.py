import numpy as np
import pandas as pd

# Make results reproducible
np.random.seed(42)

# Number of sensor readings
n_samples = 10000

# Generate machine sensor data
temperature = np.random.normal(70, 8, n_samples)
vibration = np.random.normal(0.20, 0.08, n_samples)
current = np.random.normal(5, 0.8, n_samples)
rpm = np.random.normal(1500, 80, n_samples)

# Identify abnormal machine conditions
failure_risk = (
    (temperature > 85)
    | (vibration > 0.40)
    | (current > 7)
    | (rpm < 1350)
)

# Convert True/False into 1/0
machine_status = failure_risk.astype(int)

# Create DataFrame
df = pd.DataFrame({
    "temperature": temperature,
    "vibration": vibration,
    "current": current,
    "rpm": rpm,
    "machine_status": machine_status
})

# Save the dataset
df.to_csv(
    "data/raw/sensor_data.csv",
    index=False
)

print("Sensor dataset created successfully!")
print(f"Number of records: {len(df)}")

print("\nFirst 5 records:")
print(df.head())

print("\nMachine status distribution:")
print(df["machine_status"].value_counts())