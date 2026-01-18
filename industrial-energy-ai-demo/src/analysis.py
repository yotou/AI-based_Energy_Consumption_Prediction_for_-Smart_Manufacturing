import pandas as pd

# Load data
df = pd.read_csv("data/sample_data.csv")

# Basic analysis
avg_energy = df["energy_kwh"].mean()
max_temp = df["temperature"].max()
high_load_ratio = (df["load_percent"] > 80).mean()

print("Average energy consumption:", avg_energy)
print("Maximum temperature:", max_temp)
print("High load ratio:", high_load_ratio)
