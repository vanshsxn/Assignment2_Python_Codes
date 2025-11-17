import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(3)
n=200
x = np.concatenate([np.random.normal(1000, 200, n-5), np.array([5000,6000,7000,8000,9000])])
df = pd.DataFrame({"amount": x})

df["zscore"] = np.abs(stats.zscore(df["amount"]))
z_outliers = df[df["zscore"] > 3]["amount"].tolist()

Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
iqr_outliers = df[(df["amount"] < lower) | (df["amount"] > upper)]["amount"].tolist()

print("Z-score outliers:", z_outliers)
print("IQR outliers:", iqr_outliers)

df["amount_capped"] = df["amount"].clip(upper=upper)
print("After capping, max:", df["amount_capped"].max())
