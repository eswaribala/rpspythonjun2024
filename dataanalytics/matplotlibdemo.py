# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 07:02:58 2018

@author: Balasubramaniam
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as pl
x2=['India','Singapore','USA','UK']
x1=[1,2,3,4]
y=[1,2,3,4]
pl.plot(x1,y)
pl.xticks(x1,x2)

pl.show()


# Initialize a Figure 
fig = plt.figure()

# Add Axes to the Figure
fig.add_axes([0,0,1,1])
plt.show()


#Plotting to our canvas
plt.plot([1,2,3],[4,5,1])

#Showing what we plotted
plt.show()

x = [5,8,10]
y = [12,16,6]



plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

df=pd.read_csv("diabetes.csv")
x=df["BMI"]
y=df["Glucose"]
y1=df["BloodPressure"]
plt.scatter(x, y, color='g')
plt.scatter(x, y1, color='m')
plt.show()





from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# can plot specifically, after just showing the defaults:
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()

plt.grid(True,color='k')

plt.show()




style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.scatter(x, y)#, align='center')

plt.scatter(x2, y2, color='g')#, align='center')


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()








#subplot
# Set up Axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Scatter the data
ax.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5))

# Show the plot
plt.show()

#change figure size

# Initialize the plot
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# or replace the three lines of code above by the following line: 
#fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

# Show the plot
plt.show()

#plotting routines
# Initialize the plot
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
#ax3.scatter(x,y)

# Show the plot
plt.show()

plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.show()
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0.5, 4.5)
plt.show()


#pie chart
'''
Syntax: matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)

Parameters:
data represents the array of data values to be plotted, the fractional area of each slice is represented by data/sum(data). If sum(data)<1, then the data values returns the fractional area directly, thus resulting pie will have empty wedge of size 1-sum(data).
labels is a list of sequence of strings which sets the label of each wedge.
color attribute is used to provide color to the wedges.
autopct is a string used to label the wedge with their numerical value.
shadow is used to create shadow of wedge.
'''
# Data to plot
labels = 'Python', 'C++', 'Ruby', 'Java'
data = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(data, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()



