import matplotlib.pyplot as plt
import numpy as np
"""years = [2010,2012,2013,2014,2015,2016,2017,2018,2019]
number_of_passengers = [5000,7000,13000,10000,20000,22000,17000,16500,27000]
plt.bar(years,number_of_passengers)
plt.xlabel('years')
plt.ylabel('number_of_passengers')
plt.xticks(years)
plt.yticks(number_of_passengers)
plt.grid(True)
plt.grid(color='b', ls = '-.', lw = 0.25)
plt.show()"""


"""income = ['16-22','23-29','30-36','37-43','44-50','51-57']
income2 = np.arange(16,57,7)
print(income2)
families = [2,3,5,8,8,10]
plt.bar(income2,families)
#plt.xticks(income)
#plt.yticks(families)
plt.show()"""


"""x = np.arange(7)
families = [2,3,5,8,8,10]
plt.bar(families, height=[2,3,5,8,8,10])
plt.xticks(families, ['16-22','23-29','30-36','37-43','44-50','51-57'])
plt.show()
"""
"""families = [2,3,5,8,8,10]
x = np.arange(16,58,1)
plt.hist(families)
plt.axis([16, 57, 2, 10])
#axis([xmin,xmax,ymin,ymax])
plt.xlabel('Weight')
plt.ylabel('Probability')
plt.show()
plt.hist"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(16,58,7)
print(x)
families = [2,3,5,8,8,10]
#plt.hist(x,bins=10,weights =families,rwidth=6 )
#plt.show()
y = [2,3,5,8,8,10]
x = ['16-22','23-29','30-36','37-43','44-50','51-57']
#plt.bar(x,y)
plt.bar(x, y, 1, color='r')
plt.show()

"""import numpy as np
import matplotlib.pyplot as plt

alphab = ['16-22','23-29','30-36','37-43','44-50','51-57']
frequencies = [2,3,5,8,8,10]

pos = np.arange(len(alphab))
width = 1.0     # gives histogram aspect to the bar diagram

ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(alphab)

plt.bar(pos, frequencies, width, color='r')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
Income = ['16','22', '29', '36', '43', '50', '57']
NumberofFamilies = [0,2, 3, 5, 8, 8, 10]
pos = np.arange(len(Income))
width = 1.0     # gives histogram aspect to the bar diagram
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(Income)
plt.bar(Income, NumberofFamilies, width)
plt.show()"""