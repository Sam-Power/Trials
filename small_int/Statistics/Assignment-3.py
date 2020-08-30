"""EXERCISE 1. The following data represent responses from 20 students who were asked “How many hours are you studying in a week?”
16	15	12	15	10	16	16	15	15	15	12	18	12	14	10	18	15	14	15	15
What is the value of the mode? The median? The mean?
EXERCISE 2. Use the data below to calculate the mean, variance, and standard deviation.
10	9	7	9	8	9	5	4
EXERCISE 3. The list named as salary represents the yearly income for some data scientists in USA.
salary = [120, 80, 85, 85, 80, 83, 100, 105, 105, 85, 75, 125, 120, 105, 85, 80, 95, 90, 95, 85, 80, 85, 120, 100, 105, 90]
Calculate the mean, median, mode, range, interquartile range, variance, and standard deviation in Python. What can you conclude from these measures?"""
#EXERCISE 1.
import numpy as np
import scipy.stats as stats
print("#EXERCISE 1")
data = [16,15,	12,	15,	10,	16,	16,	15,	15,	15,	12,	18	,12	,14	,10	,18	,15	,14,15,15]
print(f"mode: {stats.mode(data)}")
print(f"median : {np.median(data)}")
print(f"mean : {np.mean(data)}")

#EXERCISE 2
print("#EXERCISE 2")
data = [10	,9,	7,	9	,8	,9	,5	,4]
print(f"mean : {np.mean(data)}")
print(f"var : {np.var(data)}")
print(f"std : {np.std(data)}")

#EXERCISE 3
print("#EXERCISE 3")
salary = [120, 80, 85, 85, 80, 83, 100, 105, 105, 85, 75, 125, 120, 105, 85, 80, 95, 90, 95, 85, 80, 85, 120, 100, 105, 90]
print(f"mean : {np.mean(salary)}")
print(f"median : {np.median(salary)}")
print(f"mode : {stats.mode(salary)}")
print(f"range : {max(salary) - min(salary)}")
print(f"iqr : {stats.iqr(salary)}")
print(f"std : {np.std(salary)}")

