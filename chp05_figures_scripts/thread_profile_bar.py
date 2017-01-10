# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:22:29 2016

@author: dav
"""

import numpy as np
import matplotlib.pyplot as plt

N = 4

UseTimes = (22.1, 12.5, 2.1, 10.2)
SpinTimes = (11.6, 1.8, 0.1, 8.4)
OvrheadTimes = (0.4, 0.4, 0.4, 0.0)

index = np.arange(N)
barwidth = 0.35

p1 = plt.bar(index, UseTimes, barwidth, color='g')
p2 = plt.bar(index, SpinTimes, barwidth, color='y')
p3 = plt.bar(index, OvrheadTimes, barwidth, color='r')

plt.ylabel('Time (%)')
plt.xticks(index + barwidth/2., ('erode', 'flow_route', 'scan_area', 'depth_update'))
plt.yticks(np.arange(0, 30, 5))
plt.legend((p1[0], p2[0], p3[0]), ('Parallel execution time', 'Load imbalance', 'Overheads'))

plt.show()