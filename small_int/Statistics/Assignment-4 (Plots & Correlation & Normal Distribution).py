"""EXERCISE 1. Use the data in the table below to generate a scatter plot, calculate Pearson’s correlation, and interpret the relationship between two variables.

X	Y
0	88
6	52
 4	64
 1	60
 5	54
 3	78
 4	40
EXERCISE 2.In some cases we, data analysts, make calculations using online calculators. Answer the following questions using the online calculator available at this link: Normal Distribution Calculator

The heights of male students in a particular town are normally distributed with a mean of 65 inches and a standard deviation of 1.7. What percentage of these students is taller than 66.7 inches?
A data set was created by asking 300 students about their weights. The mean is 60 kg. standard deviation is 8 kg. How many students weighed more than 52 kg and less than 68 kg?
EXERCISE 3. The last 10 game results between LA Lakers and LA Clippers are given in the table below. Draw two boxplots for the points scored by these 2 teams.

Date	LA Lakers	LA Clippers
July 31, 2020	103	101
March 8, 2020	112	103
December 26, 2019	106	111
October 23, 2019	102	112
July 7, 2019	87	93
April 6, 2019	122	117
March 5, 2019	105	113
February 1, 2019	123	120
December 29, 2018	107	118
October 7, 2018	87	103
Which team has a greater median, Lakers or Clippers?
Which team has greater IQR, Lakers or Clippers?
Which team has a higher percentage of scores above its median?"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

x = np.array([0,6,4,1,5,3,4])
y= np.array([88,52,64,60,54,78,40])

plt.scatter(x,y)
plt.show()

a = scipy.stats.pearsonr(x, y)
b = np.corrcoef(x,y)[0,1]
c = np.cov(x,y)

print(a)
print("-----")
print(b)
print("-----")
print(c)

LA_Lakers = np.array([103,112,106,102,87,122,105,123,107,87])
LA_Clippers = np.array([101,103,111,112,93,117,113,120,118,103])
fig,axes = plt.subplots(1,2)
axes[0].boxplot(LA_Lakers)
axes[0].set_title("LA LAKERS")
axes[1].boxplot(LA_Clippers)
axes[1].set_title("LA CLIPPERS")
plt.show()