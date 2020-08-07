import matplotlib as mpl

import  numpy as np
import matplotlib.pyplot as plt
data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
print(group_data)
group_names = list(data.keys())
print(group_names)
group_mean = np.mean(group_data)
print(group_mean)
fig, ax = plt.subplots(figsize=(8,4))
plt.style.use('fivethirtyeight')
plt.rcParams.update({'figure.autolayout': True})
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation = 45, horizontalalignment = 'right')
ax.set(xlim=[-10000, 140000], xlabel = 'Total Revenue', ylabel = 'Company',
       title = 'Company Renvenue')
#plt.show()
print(fig.canvas.get_supported_filetypes())
#fig.savefig('sales.png')
import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)
