# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:45:58 2016

@author: http://chrisalbon.com/python/matplotlib_stacked_bar_plot.html

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def init_plotting():
    plt.rcParams['figure.figsize'] = (8, 8)
    plt.rcParams['font.size'] = 16
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['axes.labelsize'] = 1.4*plt.rcParams['font.size']
    plt.rcParams['axes.titlesize'] = 1.5*plt.rcParams['font.size']
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

#    plt.gca().spines['right'].set_color('none')
#    plt.gca().spines['top'].set_color('none')
#    plt.gca().xaxis.set_ticks_position('bottom')
#    plt.gca().yaxis.set_ticks_position('left')

init_plotting()


UseTimes = (22.1, 12.5, 2.1, 10.2)
SpinTimes = (11.6, 1.8, 0.1, 8.4)
OvrheadTimes = (0.4, 0.4, 0.4, 0.0)

raw_data = {"function": ['erode', 'flow_route', 'scan_area', 'depth_update'],
            "use_times": [22.1, 12.5, 2.1, 10.2],
            "spin_times": [11.6, 1.8, 0.1, 8.4],
            "overhead_times": [0.4, 0.4, 0.4, 0.0]}

dataframe = pd.DataFrame(raw_data,
                         columns=['function', 'use_times',
                                  'spin_times', 'overhead_times'])


f, ax1 = plt.subplots(1,figsize=(10,5))

barwidth = 0.5

bar_left = [i+1 for i in range(len(dataframe["use_times"]))]

tick_pos = [i+(barwidth/2) for i in bar_left]

# Create a bar plot, in position bar_1
ax1.bar(bar_left,
        # using the pre_score data
        dataframe['use_times'],
        # set the width
        width=barwidth,
        # with the label pre score
        label='Parallel execution time',
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F4561D')


# Create a bar plot, in position bar_1
ax1.bar(bar_left,
        # using the mid_score data
        dataframe['spin_times'],
        # set the width
        width=barwidth,
        # with pre_score on the bottom
        bottom=dataframe['use_times'],
        # with the label mid score
        label='Load imbalance',
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F1911E')

# Create a bar plot, in position bar_1
ax1.bar(bar_left,
        # using the post_score data
        dataframe['overhead_times'],
        # set the width
        width=barwidth,
        # with pre_score and mid_score on the bottom
        bottom=[i+j for i,j in zip(dataframe['use_times'], dataframe['spin_times'])],
        # with the label post score
        label='Overhead time',
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F1BD1A')

# set the x ticks with names
plt.xticks(tick_pos, dataframe['function'])

# Set the label and legends
ax1.set_ylabel("Model run time (%)")
ax1.set_xlabel("Function")
plt.legend(loc='upper right')

plt.xlim([min(tick_pos)-barwidth, max(tick_pos)+barwidth])

plt.show()