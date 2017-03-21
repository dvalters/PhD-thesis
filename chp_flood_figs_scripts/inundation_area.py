#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:31:03 2017

Plots ensemble graphs from the inundation metric generator

@author: dav
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import glob
import re
import os
import itertools

marker = itertools.cycle(('^', 'D', 's', 'o')) 

plt.rcParams['axes.color_cycle'] = ['darkorchid', 'darkturquoise', 'seagreen', 'blue']
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.labelsize'] = 1.2*plt.rcParams['font.size']
plt.rcParams['axes.titlesize'] = 1.2*plt.rcParams['font.size']
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']



bos_file_wildcard = "/mnt/SCRATCH/Analyses/InundationAnalysis/BoscastleInundation/boscastle_inundation_*.txt"
rye_file_wildcard = "/mnt/SCRATCH/Analyses/InundationAnalysis/RyedaleInundation/ryedale_inundation_*.txt"


def make_line_label(fname):
    # Passing a list of delimiters to the re.split function
    
    basename = os.path.splitext(os.path.basename(fname))
    print(basename)
    parts = re.split("[_]", basename[0])

    #part = basename[0] + '_' + basename[1]
    print(parts[2] + '_' + parts[3])
    label = parts[2] + '_' + parts[3]
    return label

def convert_timestep(time_step):
    #minutes = time_step*5
    hours = time_step/60
    return hours

fig, axarr = plt.subplots(2)

"""Boscastle plots"""
for file in sorted(glob.glob(bos_file_wildcard)):
    print(file)
    timestep, inundation_area, catchment_depth, floodplain_depth, channel_depth = \
      np.loadtxt(file, usecols=(0,1,2,3, 4) , unpack=True)
    
    hours = convert_timestep(timestep)
    label = make_line_label(file)
    line, = axarr[0].plot(hours, inundation_area*1e-6, marker=marker.__next__(), linestyle='', alpha=0.7)
    print(line)
    line.set_label(label)

axarr[0].legend(loc="upper left")  
#axarr[0].set_ylim(-0.2, 3.0)
axarr[0].set_ylabel("Inundation area (km$^2$)")
axarr[0].set_title("Boscastle")

"""Ryedale plots"""
for file in sorted(glob.glob(rye_file_wildcard)):
    print(file)
    timestep, inundation_area, catchment_depth, floodplain_depth, channel_depth = \
      np.loadtxt(file, usecols=(0,1,2,3, 4) , unpack=True)
    
    hours = convert_timestep(timestep)
    label = make_line_label(file)
    line, = axarr[1].plot(hours, inundation_area*1e-6, marker=marker.__next__(), linestyle='', alpha=0.7)
    print(line)
    line.set_label(label)

axarr[1].legend(loc="upper left") 
axarr[1].set_title("Ryedale") 
axarr[1].set_ylabel("Inundation area (km$^2$)")
axarr[1].set_xlabel("Hours after simulation start")
#axarr[1].set_ylim(-0.2, 3.0)
    