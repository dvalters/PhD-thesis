# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:56:54 2016

@author: dav
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def init_plotting():
    plt.rcParams['figure.figsize'] = (8, 8)
    plt.rcParams['font.size'] = 17
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['axes.labelsize'] = 1.2*plt.rcParams['font.size']
    plt.rcParams['axes.titlesize'] = 1.2*plt.rcParams['font.size']
    plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
    plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
    plt.rcParams['savefig.dpi'] = 2*plt.rcParams['savefig.dpi']
    plt.rcParams['xtick.major.size'] = 3
    plt.rcParams['xtick.minor.size'] = 3
    plt.rcParams['xtick.major.width'] = 1
    plt.rcParams['xtick.minor.width'] = 1
    plt.rcParams['ytick.major.size'] = 3
    plt.rcParams['ytick.minor.size'] = 3
    plt.rcParams['ytick.major.width'] = 1
    plt.rcParams['ytick.minor.width'] = 1
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.loc'] = 'center left'
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['lines.linewidth'] = 1.5

#    plt.gca().spines['right'].set_color('none')
#    plt.gca().spines['top'].set_color('none')
#    plt.gca().xaxis.set_ticks_position('bottom')
#    plt.gca().yaxis.set_ticks_position('left')

init_plotting()

path = "/run/media/dav/SHETLAND/Manuscripts/GMD_LSDCatchmentModel/csv_scaling/"
file_bos48_5m = "strong_scaling_bos48hr_5m.csv"
file_bos72_2m = "strong_scaling_bos72hr_2m.csv"
file_bos72_5m = "strong_scaling_bos72hr_5m.csv"
file_swale1yr_50m = "strong_scaling_swale1yr_50m.csv"
file_weak_scaling_bos = "weak_scaling_bos.csv"

bos48_5m = pd.read_csv(path + file_bos48_5m)
bos72_2m = pd.read_csv(path + file_bos72_2m)
bos72_5m = pd.read_csv(path + file_bos72_5m)
swale1yr_50m = pd.read_csv(path + file_swale1yr_50m)
weak_scaling_bos = pd.read_csv(path + file_weak_scaling_bos)

f, ax_arr = plt.subplots(4, 1, figsize=(10, 5), sharex=True)

# Strong scaling bos 48hr 5m
l1 = ax_arr[0].plot(bos48_5m['threads'], bos48_5m['speedup_erosion'],
                     color='orange', marker='^')
l2 = ax_arr[0].plot(bos48_5m['threads'], bos48_5m['speedup_hydro'],
                     color='b', marker='^')
ax_arr[0].set_title('Boscastle 48hr simulation, 5m DEM\n720 000 grid cells')
#ax_arr[0].set_subtitle('720 000 grid cells')

# Strong scaling bos 72hr 5m
ax_arr[1].plot(bos72_5m['threads'], bos72_5m['speedup_erosion'],
                     color='orange', marker='^')
ax_arr[1].plot(bos72_5m['threads'], bos72_5m['speedup_hydro'],
                     color='b', marker='^')
ax_arr[1].set_title('Boscastle 72hr simulation, 5m DEM\n720 000 grid cells')


# Strong scaling bos 72hr 2m
l1 = ax_arr[2].plot(bos72_2m['threads'], bos72_2m['speedup_erosion'],
                     color='orange', marker='^')
l2 = ax_arr[2].plot(bos72_2m['threads'], bos72_2m['speedup_hydro'],
                     color='b', marker='^')
ax_arr[2].set_title('Boscastle 72hr simulation, 2m DEM\n4 500 000 grid cells')
#ax_arr[1].legend(loc='upper left', labels=["Erosion-enabled", "Hydrology-only"])



# Strong scaling swale 72hr 50m
ax_arr[3].plot(swale1yr_50m['threads'], swale1yr_50m['speedup_erosion'],
                     color='orange', marker='^')
ax_arr[3].plot(swale1yr_50m['threads'], swale1yr_50m['speedup_hydro'],
                     color='b', marker='^')
ax_arr[3].legend(loc='upper left', labels=["Erosion-enabled", "Hydrology-only"])
ax_arr[3].set_title('Swale 1 year simulation, 50m DEM\n124 931 grid cells')
ax_arr[3].set_xlabel('Number of threads/cores')

for i in range(0, 4):
    ax_arr[i].set_xlim(1, 50)
    ax_arr[i].set_ylim(0, 16)
    ax_arr[i].set_ylabel('Speed-up')

#plt.figlegend( (l1, l2), ('Erosion', 'Hydro'), 'upper left' )
plt.show()