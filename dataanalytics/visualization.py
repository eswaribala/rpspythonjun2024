import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(filepath_or_buffer="diabetics.csv")
x=data["BMI"]
y=data["Glucose"]
plt.figure()
plt.title("BMI vs Glucose")
plt.scatter(x,y)
plt.grid(True,color='k')
plt.show()
labels = 'Python', 'C++', 'Ruby', 'Java'
data = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
# Plot
plt.pie(data, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.pie(data,shadow=True, startangle=140)
plt.show()
