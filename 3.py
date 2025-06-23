import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print("1D:", a1)
print("2D:\n", a2)
print("Add 10:", a1 + 10)
print("Mul *2:\n", a2 * 2)
print("Slice 1D:", a1[1:4])
print("Slice 2D Col1:", a2[:, 1])
print("Reshape:\n", a1.reshape(-1, 1))
print("Sum:", np.sum(a2), "| Mean:", np.mean(a2))
print("Transpose:\n", a2.T)
print("Broadcast + [10,20,30]:\n", a2 + np.array([10, 20, 30]))

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'Age': [24, 30, 22, 35],
                   'Salary': [50000, 60000, 55000, 65000]})
print("\nDataFrame:\n", df)
print("\nInfo:")
print(df.info())
print("\nStats:\n", df.describe())
print("Age > 25:\n", df[df.Age > 25])
df['Bonus'] = df['Salary'] * 0.1
print("With Bonus:\n", df)
print("Mean Salary:", df['Salary'].mean())
print("Sorted by Age:\n", df.sort_values('Age'))

df2 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'Eve'],
                    'Department': ['HR', 'IT', 'Finance', 'Marketing']})
merged = pd.merge(df, df2, on='Name', how='inner')
print("\nMerged DataFrame (on 'Name'):\n", merged)

x = np.arange(1, 6)
y = np.array([10, 15, 7, 10, 12])
rand_data = np.random.randn(1000)
rand_err = np.random.rand(len(y)) * 2
df_dens = pd.DataFrame({c: np.random.randint(1, 10, 100) for c in "ABC"})

plt.figure(); plt.plot(x, y, 'bo-'); plt.title("Line"); plt.grid(); plt.show()
plt.figure(); plt.bar(x, y, color='g'); plt.title("Bar"); plt.show()
plt.figure(); plt.pie([15,30,45,10], labels=['A','B','C','D'], autopct='%1.1f%%'); plt.title("Pie"); plt.show()
plt.figure(); plt.scatter(x, y, c='r'); plt.title("Scatter"); plt.show()
plt.figure(); plt.hist(rand_data, bins=30, color='purple', alpha=0.7); plt.title("Histogram"); plt.show()
plt.figure(); plt.boxplot(rand_data); plt.title("Box"); plt.show()
plt.figure(); [sns.kdeplot(df_dens[c], label=c, fill=True, alpha=0.3) for c in df_dens]; plt.title("Density"); plt.legend(); plt.show()
plt.figure(); plt.errorbar(x, y, yerr=rand_err, fmt='o', ecolor='red', capsize=5); plt.title("Error Bar"); plt.show()

X, Y = np.meshgrid(np.linspace(0, 2, 30), np.linspace(0, 2, 30))
Z = np.sin(X*np.pi) * np.cos(Y*np.pi)
plt.figure(); c = plt.contour(X, Y, Z, cmap='viridis'); plt.clabel(c); plt.title("Contour"); plt.show()

print("\nAll operations and plots completed.")
