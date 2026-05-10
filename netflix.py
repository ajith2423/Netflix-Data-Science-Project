# Netflix Data Cleaning & Visualization Project
# Author: Ajith Kumar S

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Display First 5 Rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# -----------------------------
# DATA CLEANING
# -----------------------------

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Not Available", inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['rating'].fillna("Not Rated", inplace=True)

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Date Column
df['date_added'] = pd.to_datetime(df['date_added'])

# Create New Columns
df['year_added'] = df['date_added'].dt.year

# -----------------------------
# DATA VISUALIZATION
# -----------------------------

# 1. Movies vs TV Shows
plt.figure(figsize=(6,5))

sns.countplot(x='type', data=df)

plt.title("Movies vs TV Shows on Netflix")

plt.show()

# 2. Content Added Per Year
plt.figure(figsize=(12,6))

df['year_added'].value_counts().sort_index().plot(kind='line', marker='o')

plt.title("Netflix Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Count")

plt.grid(True)

plt.show()

# 3. Top 10 Countries
plt.figure(figsize=(10,6))

top_countries = df['country'].value_counts().head(10)

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Shows/Movies")
plt.ylabel("Country")

plt.show()

# 4. Ratings Distribution
plt.figure(figsize=(10,6))

sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)

plt.title("Content Ratings Distribution")

plt.show()

# 5. Heatmap
plt.figure(figsize=(8,5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# Save Cleaned Dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("\nNetflix Data Cleaning & Visualization Completed Successfully!")
