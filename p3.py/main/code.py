# MINI DATA ANALYSIS PROJECT (Simple Version)

import os
import pandas as pd
import matplotlib.pyplot as plt

file_name = "sales_data.csv"

# ------------------------------------------------
# STEP 1: Create sample file if not exists
# ------------------------------------------------
if not os.path.exists(file_name):
    data = {
        "Category": ["Electronics", "Clothing", "Furniture", "Electronics", "Clothing"],
        "Sales": [50000, 20000, 30000, 40000, 25000],
        "Profit": [5000, 2000, 3000, 4000, 2500]
    }
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
    print("Sample sales_data.csv created successfully!")

# ------------------------------------------------
# STEP 2: Load Data
# ------------------------------------------------
df = pd.read_csv(file_name)

# ------------------------------------------------
# STEP 3: Clean Data
# ------------------------------------------------
df = df.drop_duplicates()
df.fillna(df.mean(numeric_only=True), inplace=True)

# ------------------------------------------------
# STEP 4: Show Summary
# ------------------------------------------------
print("\nData Summary:")
print(df.describe())

# ------------------------------------------------
# STEP 5: Visualization
# ------------------------------------------------

# Sales by Category
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.show()

# Profit Distribution
df["Profit"].plot(kind="hist", bins=5)
plt.title("Profit Distribution")
plt.show()

print("\nProject Completed Successfully 🎉")
