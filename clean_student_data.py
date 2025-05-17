
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/student_data.csv')

# Show basic info before cleaning
print("Initial Data Overview:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# -------------------------------
# 1. Handle Missing Numerical Values
# -------------------------------
# Fill numeric scores with mean
numeric_cols = ['math_score', 'english_score', 'age']
for col in numeric_cols:
    if col in df.columns:
        df[col].fillna(df[col].mean(), inplace=True)

# -------------------------------
# 2. Handle Missing Categorical Values
# -------------------------------
# Fill 'gender' with mode
if 'gender' in df.columns:
    df['gender'].fillna(df['gender'].mode()[0], inplace=True)
    # Standardize text format
    df['gender'] = df['gender'].str.strip().str.lower()

# -------------------------------
# 3. Handle Missing Critical Identifiers
# -------------------------------
# Drop rows where 'name' is missing
if 'name' in df.columns:
    df.dropna(subset=['name'], inplace=True)

# -------------------------------
# 4. Handle Attendance
# -------------------------------
if 'attendance' in df.columns:
    df['attendance'].fillna(df['attendance'].mode()[0], inplace=True)

# -------------------------------
# 5. Remove Duplicates
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# 6. Summary After Cleaning
# -------------------------------
print("\nAfter Cleaning:")
print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# -------------------------------
# 7. Save Cleaned Dataset
# -------------------------------
df.to_csv('data/cleaned_student_data.csv', index=False)
print("\nCleaned data saved to 'data/cleaned_student_data.csv'.")

# -------------------------------
# 8. Optional: Visualize Missing Data (Before Cleaning)
# -------------------------------
# Reload original data to show heatmap
original_df = pd.read_csv('data/student_data.csv')
plt.figure(figsize=(10, 6))
sns.heatmap(original_df.isnull(), cbar=False, cmap='Reds')
plt.title("Missing Values Heatmap (Before Cleaning)")
plt.savefig('images/missing_data_heatmap.png')
print("Missing data heatmap saved to 'images/missing_data_heatmap.png'.")
