# invoke the module
from ecommercelib.userlib.arrayfromexcel import gendata

# read from console
startrow = int(input("Enter Start Row Value"))
endrow = int(input("Enter End Row Value"))
col = int(input("Enter Column Value"))
data = gendata(startrow, endrow, col,
               filepath="F:/Local disk/pythoninteljun2024/AdvancePythonTraining/resources/GDP.xlsx", sheetname="GDP")

#print(data)

import statistics

# total GDP
print("Total GDP %d" % (sum(data)))
print("Average GDP %d" % (statistics.mean(data)))
print("Min GDP %d" % (min(data)))
print("Max GDP %d" % (max(data)))