import pandas as pd
import numpy as np
# gen data frame
data_frame = pd.read_csv(filepath_or_buffer="Data.csv")

print("Salary Count\n", data_frame["Salary"].count())
print("Sum Salary\n", data_frame["Salary"].sum())
print("Minimum Salary\n", data_frame["Salary"].min())
print("Maximum Salary\n", data_frame["Salary"].max())

# first 5 rows
print("First 5 Rows", data_frame.head(5))
# last 5 rows
print("Last 5 Rows", data_frame.tail(5))

# missing data
#selects all the column except the last col
x = data_frame.iloc[:, :-1].values
#selects only the last column
y = data_frame.iloc[:, -1].values
print("X Value from Data Frame\n", x)
print("Y Value from Data Frame\n", y)
from sklearn.impute import SimpleImputer
simple_imputer=SimpleImputer(missing_values=np.nan, strategy='median')
x[:, 1:3] = simple_imputer.fit_transform(x[:, 1:3])

print("Age after imputer\n",x[:, 1])
print("Salary after imputer\n",x[:, 2])