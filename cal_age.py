'''age = int(input("enter your age: "))
Name = str(input("enter your name: "))
year = str((2020 - age) + 100)
print("your name is", Name + "  and you are ", age, " years old")
print(Name, "will be 100 years old in the year " + year)'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
from cycler import cycler
data = np.random.randn(20)
'''with plt.style.context('dark_background', 'presenataion'):
    plt.plot(np.random.randn(20), 'r-o')'''
#plt.show()
'''mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
plt.plot(data)'''
#mpl.rcParams['axes.prop_cycle'] = cycler(color = ['g','r'])
#mpl.rc('lines', linewidth= 4, linestyle='-.')
#plt.plot(data)
#plt.show()
matplotlib.matplotlib_fname()