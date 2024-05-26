import matplotlib
# matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
labels = 'A','B','C','D'
sizes = [10,20,10,60]
plt.pie(sizes,labels=labels,explode = (0,0.1,0,0),autopct='%1.1f')
plt.show()