import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(2)
n = 600
df = pd.DataFrame({
    "age": np.random.randint(20, 80, n),
    "salary": np.concatenate([np.random.normal(50000, 10000, n-10), np.random.normal(200000, 5000, 10)]),
    "expenses": np.random.normal(20000, 5000, n)
})

df.loc[2, "salary"] = None
df.loc[50:55, "expenses"] = df.loc[50:55, "expenses"] * 5

print("Missing values per column:")
print(df.isna().sum())

df["salary"].fillna(df["salary"].median(), inplace=True)

plt.figure()
plt.hist(df["salary"], bins=40)
plt.title("Histogram of Salary")
plt.show()

plt.figure()
sns.boxplot(x=df["expenses"])
plt.title("Boxplot of Expenses")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

Q1 = df["expenses"].quantile(0.25)
Q3 = df["expenses"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
df["expenses_capped"] = df["expenses"].clip(lower, upper)

print(df.describe())

# Final insight summary printed
print("""
Final insights:
1. There is a cluster of unusually high salaries for a small subset (possible executive group or data error). 
2. Expenses show several high outliers likely due to anomalous transactions; capping reduces skew and stabilizes averages.
3. Salary and expenses correlate weakly; raising salary does not linearly increase expenses for most users, implying savings potential.
4. Median salary replacement for missing values is reasonable when missingness is sparse and likely random.
5. For business decisions: consider flagging high-salary/high-expense users for premium offers and financial planning services.
6. Apply targeted outreach (budget coaching) to users with expenses near the capped threshold to reduce churn and defaults.
""")
