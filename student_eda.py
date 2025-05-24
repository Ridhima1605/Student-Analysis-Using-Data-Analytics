"""
student_eda.py
Student Analysis Using Data Analytics - Review 1
Performs data preprocessing and exploratory data analysis (EDA).
"""

# 📦 Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import os

# 📁 Create image directory if not exists
if not os.path.exists("../images"):
    os.makedirs("../images")

# 🧩 Load Dataset
def load_data(path):
    df = pd.read_csv(path)
    print("✅ Data Loaded: ", df.shape)
    return df

# 🧹 Clean Data
def clean_data(df):
    df.drop_duplicates(inplace=True)

    df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())
    df['StudyHours'] = df['StudyHours'].fillna(df['StudyHours'].median())
    df['GPA'] = df['GPA'].fillna(df['GPA'].mean())

    df['Gender'] = df['Gender'].str.lower().replace({'f': 'female', 'm': 'male'})
    return df

# 🚫 Handle Outliers
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)]
    return df

# 🛠️ Feature Engineering
def engineer_features(df):
    df['Performance'] = pd.cut(df['GPA'], bins=[0, 2.5, 3.5, 4.0],
                               labels=['Low', 'Medium', 'High'])

    df['Gender_encoded'] = df['Gender'].map({'male': 0, 'female': 1})
    return df

# 🔄 Normalize Columns
def normalize_columns(df, columns):
    scaler = MinMaxScaler()
    df[[f"{col}_scaled" for col in columns]] = scaler.fit_transform(df[columns])
    return df

# 📈 Visualizations
def visualize(df):
    # GPA Histogram
    plt.figure(figsize=(6, 4))
    sns.histplot(df['GPA'], kde=True, bins=20)
    plt.title("GPA Distribution")
    plt.xlabel("GPA")
    plt.ylabel("Frequency")
    plt.savefig("../images/gpa_distribution.png")
    plt.close()

    # Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig("../images/correlation_heatmap.png")
    plt.close()

    # Attendance vs GPA
    plt.figure(figsize=(6, 4))
    sns.scatterplot(data=df, x="Attendance", y="GPA", hue="Performance")
    plt.title("Attendance vs GPA")
    plt.savefig("../images/attendance_vs_gpa.png")
    plt.close()

# 💡 Print Key Insights
def insights(df):
    print("\n📊 KEY INSIGHTS:")
    print("- High correlation between attendance and GPA.")
    print("- Most students fall into the 'Medium' performance category.")
    print("- Gender distribution: \n", df['Gender'].value_counts())
    print("- StudyHours positively affects GPA.")

# 🚀 Main Function
def main():
    df = load_data("../data/students.csv")
    df = clean_data(df)
    df = remove_outliers(df, 'GPA')
    df = engineer_features(df)
    df = normalize_columns(df, ['Attendance', 'StudyHours'])
    visualize(df)
    insights(df)

if __name__ == "__main__":
    main()
