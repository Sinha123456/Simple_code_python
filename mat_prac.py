import matplotlib.pyplot as plt
import numpy as np
def identify_axes(ax_dict, fontsize=48):
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)
        # ax_dict : Dict[str, Axes]

np.random.seed(100)
hist_data = np.random.randn(50)
fig = plt.figure(constrained_layout=True)
ax_array = fig.subplots(2,2, squeeze=False)

ax_array[0,0].bar(['a','b','c'], [5,7,8])
ax_array[0,1].plot([1,2,3])
ax_array[1,0].hist(hist_data, bins='auto')
ax_array[1,1].imshow([[1,2],[2,1]])

identify_axes(
    {(j,k): a for j, r in enumerate(ax_array) for k, a in enumerate(r)}
)

#plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top = 0.85)

#set the titles for the figure and the subplot respectively
fig.suptitle('bold figure subtitle', fontsize = 14, fontweight= 'bold')
ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
#set both x- and y-axis limits to [0,10] instead of default[0,1]
ax.axis([0,10,0,10])
ax.text(3,8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
ax.text(2,6, r'an equation: $E=mc^2$', fontsize=15)
ax.text(0.95,0.01, 'colored text in axes coords',
        verticalalignment='bottom',horizontalalignment='right',
        transform=ax.transAxes, color='green', fontsize=15)
ax.plot([2],[1], 'o')
ax.annotate('annotate', xy=(2,1), xytext=(3,4),
            arrowprops=dict(facecolor='black'))
plt.show()