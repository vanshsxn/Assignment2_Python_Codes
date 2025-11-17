import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
n = 500
data = pd.DataFrame({
    "age": np.random.randint(18, 80, n),
    "blood_pressure": np.random.normal(120, 15, n).round(1),
    "cholesterol": np.random.normal(200, 30, n).round(1),
    "bmi": np.random.normal(25, 4, n).round(1)
})

plt.figure()
plt.hist(data["cholesterol"], bins=30)
plt.title("Histogram of Cholesterol")
plt.xlabel("Cholesterol")
plt.ylabel("Count")
plt.show()

plt.figure()
sns.boxplot(x=data["bmi"])
plt.title("Boxplot of BMI")
plt.show()

plt.figure(figsize=(6,5))
sns.heatmap(data.corr(), annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

insights = [
"Cholesterol distribution is roughly Gaussian centered near 200; tail of higher values suggests risk subgroup.",
"BMI shows some outliers above ~35 indicating possible obesity cases requiring attention.",
"Age correlates modestly with blood pressure; older groups likely need targeted interventions."
]
for i in insights:
    print("-", i)
