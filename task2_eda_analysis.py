# task2_eda_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set seaborn style
sns.set(style="whitegrid")

# Create output folder for charts
os.makedirs("eda_outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# ----- 1. Summary Statistics -----
print("\n📊 Summary Statistics:\n")
print(df.describe(include="all"))

# ----- 2. Age Distribution -----
sns.histplot(df['Age'].dropna(), kde=True, color='skyblue')
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("eda_outputs/age_distribution.png")
plt.clf()

# ----- 3. Fare Boxplot -----
sns.boxplot(x=df['Fare'], color='lightgreen')
plt.title("Boxplot of Fare")
plt.xlabel("Fare")
plt.savefig("eda_outputs/fare_boxplot.png")
plt.clf()

# ----- 4. Survival Count by Passenger Class -----
sns.countplot(x='Pclass', hue='Survived', data=df, palette='Set2')
plt.title("Survival Count by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.savefig("eda_outputs/survival_by_class.png")
plt.clf()

# ----- 5. Correlation Heatmap -----
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("eda_outputs/correlation_matrix.png")
plt.clf()

# ----- 6. Pairplot -----
selected_features = ['Age', 'Fare', 'Pclass', 'Survived']
sns.pairplot(df[selected_features].dropna(), hue='Survived', palette='husl')
plt.savefig("eda_outputs/pairplot.png")
plt.clf()

# ----- 7. Print Key Correlation Insights -----
print("\n📈 Correlation with Survived:\n")
print(corr['Survived'].sort_values(ascending=False))

print("\n✅ EDA Completed. All plots saved to 'eda_outputs/' folder.\n")
