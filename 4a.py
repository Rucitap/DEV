import pandas as pd

df = pd.read_csv("C:/Users/rrpro/Downloads/city_temperature.csv", low_memory=False)

df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']], errors='coerce')

df = df[df['AvgTemperature'] != -99]

df.loc[:, 'Temperature_C'] = (df['AvgTemperature'] - 32) * 5 / 9

weekly = df.groupby(['City', pd.Grouper(key='Date', freq='W')])['Temperature_C'].sum().reset_index()

weekly['Month'] = weekly['Date'].dt.to_period('M')

monthly_sum = weekly.groupby(['City', 'Month'])['Temperature_C'].sum().reset_index()

print("📌 Step 1: Monthly Sum of Temperatures by City")
print(monthly_sum.head(10))

pivot_table = monthly_sum.pivot(index='City', columns='Month', values='Temperature_C').fillna(0)

pivot_table['Total'] = pivot_table.sum(axis=1)
top_city = pivot_table['Total'].idxmax()

print("\n📊 Step 2: Month-wise Summary Table")
print(pivot_table)

print(f"\n🏆 Step 3: City with the Highest Total Temperature: {top_city}")
