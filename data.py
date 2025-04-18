import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("6640_source_data.csv")

# Show first few rows
print("First 5 rows of data:")
print(df.head())

# Check column names
print("\nColumn Names:")
print(df.columns)

# Clean the 'Year' column
df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Drop rows with missing values in important columns
df.dropna(subset=[
    'Year',
    'Minimum Concentration of Sulphur Dioxide (SO2) (24-hourly average)',
    'Maximum Concentration of Sulphur Dioxide (SO2) (24-hourly average)',
    'Concentration of Sulphur Dioxide (SO2) (Annual average)'
], inplace=True)

# Convert numeric columns
df['Year'] = df['Year'].astype(int)
df['Minimum Concentration of Sulphur Dioxide (SO2) (24-hourly average)'] = df['Minimum Concentration of Sulphur Dioxide (SO2) (24-hourly average)'].astype(float)
df['Maximum Concentration of Sulphur Dioxide (SO2) (24-hourly average)'] = df['Maximum Concentration of Sulphur Dioxide (SO2) (24-hourly average)'].astype(float)
df['Concentration of Sulphur Dioxide (SO2) (Annual average)'] = df['Concentration of Sulphur Dioxide (SO2) (Annual average)'].astype(float)

# ========== 🎯 Objectives with Visualizations ========== #

# 1. Bar plot: Average SO2 concentration by year
plt.figure(figsize=(10, 5))
df.groupby('Year')['Concentration of Sulphur Dioxide (SO2) (Annual average)'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Annual SO2 Concentration by Year')
plt.ylabel('SO2 Concentration (Annual Avg)')
plt.xlabel('Year')
plt.tight_layout()
plt.show()

# 2. Boxplot: Variation of SO2 concentration across different states
plt.figure(figsize=(14, 6))
sns.boxplot(data=df, x='srcStateName', y='Concentration of Sulphur Dioxide (SO2) (Annual average)')
plt.xticks(rotation=90)
plt.title('SO2 Concentration by State')
plt.tight_layout()
plt.show()

# 3. Scatter plot: Max vs Min SO2 concentration (24-hour average)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df,
                x='Minimum Concentration of Sulphur Dioxide (SO2) (24-hourly average)',
                y='Maximum Concentration of Sulphur Dioxide (SO2) (24-hourly average)',
                hue='Year',
                palette='viridis')
plt.title('Min vs Max 24-hour SO2 Concentration')
plt.tight_layout()
plt.show()

# 4. Histogram: Distribution of annual SO2 concentration
plt.figure(figsize=(8, 5))
sns.histplot(df['Concentration of Sulphur Dioxide (SO2) (Annual average)'], kde=True, color='green')
plt.title('Distribution of Annual SO2 Concentration')
plt.xlabel('Annual Average SO2')
plt.tight_layout()
plt.show()

# 5. Heatmap: Correlation matrix of numeric features
plt.figure(figsize=(8, 6))
corr = df[['Minimum Concentration of Sulphur Dioxide (SO2) (24-hourly average)',
           'Maximum Concentration of Sulphur Dioxide (SO2) (24-hourly average)',
           'Concentration of Sulphur Dioxide (SO2) (Annual average)',
           'Number of Monitoring Days']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of SO2 Metrics')
plt.tight_layout()
plt.show()

# 6. Line plot: Trend of SO2 annual average over time
plt.figure(figsize=(10, 5))
df.groupby('Year')['Concentration of Sulphur Dioxide (SO2) (Annual average)'].mean().plot(marker='o')
plt.title('Trend of SO2 Annual Average Over Years')
plt.ylabel('SO2 (Annual Avg)')
plt.grid()
plt.tight_layout()
plt.show()

# 7. Bar plot: Top 10 cities with highest annual average SO2
top_cities = df.groupby('City name')['Concentration of Sulphur Dioxide (SO2) (Annual average)'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_cities.plot(kind='bar', color='salmon')
plt.title('Top 10 Cities with Highest SO2 Annual Average')
plt.ylabel('Annual Average SO2')
plt.tight_layout()
plt.show()

# 8. Boxplot: SO2 concentration distribution by year
plt.figure(figsize=(12, 6))
sns.boxplot(x='Year', y='Concentration of Sulphur Dioxide (SO2) (Annual average)', data=df)
plt.title('Annual SO2 Concentration Distribution by Year')
plt.tight_layout()
plt.show()
