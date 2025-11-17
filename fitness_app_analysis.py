import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1)
n = 300
df = pd.DataFrame({
    "Age": np.random.randint(18, 65, n),
    "Gender": np.random.choice(["M","F"], n),
    "Steps_per_day": np.random.normal(7000, 2500, n).astype(int),
    "Sleep_Hours": np.round(np.random.normal(7, 1.2, n), 1),
    "BMI": np.round(np.random.normal(24, 3.5, n), 1),
    "Workout_minutes": np.round(np.random.exponential(30, n)).astype(int)
})

df.loc[df["Steps_per_day"] < 0, "Steps_per_day"] = 0
df.loc[df["Sleep_Hours"] < 3, "Sleep_Hours"] = 3
df.loc[df["BMI"] < 15, "BMI"] = 15

df.iloc[5:10, 2] = None
df.iloc[20, 4] = None

df["Steps_per_day"].fillna(df["Steps_per_day"].median(), inplace=True)
df["BMI"].fillna(df["BMI"].median(), inplace=True)

corr = df[["Workout_minutes","BMI","Sleep_Hours"]].corr()
print(corr)

plt.figure()
sns.scatterplot(data=df, x="Workout_minutes", y="BMI")
plt.title("Workout minutes vs BMI")
plt.show()

plt.figure()
sns.histplot(df["Steps_per_day"], bins=30)
plt.title("Distribution of Steps per Day")
plt.show()

print("Top recommendations:")
print("1. Encourage short daily workouts (15-30 min) to reduce BMI — show users small, frequent routines.")
print("2. Promote sleep hygiene programs for users with <6 hours — link sleep to recovery and performance.")
print("3. Use step challenges to raise daily steps from median to 9000 (increase cardio & energy).")
