import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc



r = [0,1,2]
men = [35,139,76]
women = [0,81,20]

bars = np.add(men, women).tolist()
names = ['Bronze','Gold','Silver']
barWidth = 0.5
	

plt.bar(r, men, bottom=women, color='blue', edgecolor='white', width=barWidth)
plt.bar(r, women, color='pink', edgecolor='white', width=barWidth)


labels = ["Men","Women"]
print(len(men), "Men")
print(len(women), "Women")



plt.legend(labels,loc=1)
plt.xticks(r, names)
plt.xlabel("Medals Count won by Canadian Men and Women in Ice Hockey since 1924")
plt.ylabel("Number of Medals")
	
plt.show()

