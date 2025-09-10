
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Math": [78, 90, 45, 80, 55],
    "Science": [65, 70, 35, 92, 60],
    "English": [89, 60, 55, 88, 50]
})

print("=== Student Dataset ===")
print(df, "\n")

print("=== Subject-wise Analysis ===")
for subject in df.columns[1:]:
    print(f"{subject} -> Avg: {df[subject].mean():.2f}, High: {df[subject].max()}, Low: {df[subject].min()}")
print()

df["Average"] = df.iloc[:, 1:].mean(axis=1)

print("=== Top 3 Students by Average Score ===")
print(df.sort_values(by="Average", ascending=False).head(3)[["Name", "Average"]], "\n")

df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("=== Final Student Data with Result ===")
print(df)
