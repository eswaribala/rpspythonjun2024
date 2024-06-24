import pandas as pd
import matplotlib.pyplot as plt
# create data frame
data = pd.read_csv("../resources/MSFT.csv")
X = data.iloc[:, 1:2]
Y = data.iloc[:, 5:6]
# opening stock
print(X)
# closing stock
print(Y)

plt.figure()
plt.title("open stock vs close stock")
plt.xlabel("Opening Stock")
plt.ylabel("Closing Stock")
plt.plot(X,Y,"b.")
#plt.axis([85,120,85,150])
plt.grid(True)
plt.show()
