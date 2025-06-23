import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\rrpro\Downloads\corporate_work_hours_productivity.csv")

grouped = df.groupby("Department")["Monthly_Hours_Worked"].sum().reset_index().sort_values(by="Monthly_Hours_Worked", ascending=False)
print("Step 1: Total Hours Worked by Each Department")
print(grouped)

simulated_dates = pd.date_range("2023-01-01", periods=365, freq='D')
df["Simulated_Date"] = np.random.choice(simulated_dates, size=len(df))
df["Month"] = pd.to_datetime(df["Simulated_Date"]).dt.to_period("M")

pivot_table = df.pivot_table(
    values="Monthly_Hours_Worked",
    index="Department",
    columns="Month",
    aggfunc="sum",
    fill_value=0
)
pivot_table["Total_Hours"] = pivot_table.sum(axis=1)
print("\nStep 2: Month-wise Summary Table")
print(pivot_table)

top_department = pivot_table["Total_Hours"].idxmax()
max_hours = pivot_table["Total_Hours"].max()
print(f"\nStep 3: Department with Highest Working Hours: {top_department} ({max_hours:.2f} hours)")
