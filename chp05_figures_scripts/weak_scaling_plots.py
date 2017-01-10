# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:56:54 2016

@author: dav
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

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
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.loc'] = 'center left'
    plt.rcParams['axes.linewidth'] = 1
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
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

f, ax_arr = plt.subplots(1, figsize=(10, 5))

# Strong scaling bos 48hr 5m
l1 = ax_arr.scatter(weak_scaling_bos['grid_cells'], weak_scaling_bos['time_hydro'],
                     color='b', marker='^',s=40)
l2 = ax_arr.scatter(weak_scaling_bos['grid_cells'], weak_scaling_bos['time_erosion'],
                     color='orange', marker='^', s=40)


ax_arr.set_xlim(0, 8e7)
ax_arr.set_ylim(0, 1200)
ax_arr.set_ylabel('Runtime (minutes)')
ax_arr.set_xlabel('Number of domain grid cells (million)')
#ax_arr.set_title('Weak scaling')

#ax_arr.xaxis.set_major_formatter(FormatStrFormatter('%.e'))
ax_arr.ticklabel_format(axis='x', style='sci')
ax_arr.xaxis.get_offset_text().set_visible(False)

ax_arr.legend(loc='upper right', labels=["Hydrology-only", "Erosion-enabled"])
plt.show()