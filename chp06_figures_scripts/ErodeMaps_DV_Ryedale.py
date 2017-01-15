#==============================================================================
# These are some scripts for testing the functionality of LSDMappingTools
#==============================================================================
# -*- coding: utf-8 -*-
"""
Created on Tue May 05 14:08:16 2015

@author: dav
"""
import glob as glob
import os.path
import numpy as np
import LSDPlottingTools as LSDP
import lsdmatplotlibextensions as mplext

import matplotlib.pyplot as plt
from matplotlib import ticker

# Get favourite plotting fonts and sizes
LSDP.init_plotting_DV()

# Truncate the colour map
trunc_cmap = mplext.colours.truncate_colormap("Blues", 0.4, 1.0)

# Option for getting a discrete colour map
#discreet_cmap = mplext.colours.discrete_colourmap(8, "Blues")
#discreet_cmap = mplext.colours.cmap_discretize(8, trunc_cmap)


#def RasterDifference(OriginalRaster, FinalRaster):
#    """
#    Subtracts FinalRaster from OriginalRaster
#    to create a 'DEM of difference'
#    """
#    Raster1 = LSDP.ReadRasterArrayBlocks(OriginalRaster,raster_band=1)
#    Raster2 = LSDP.ReadRasterArrayBlocks(FinalRaster,raster_band=1)
#    
#    NewRaster = np.subtract(Raster2,Raster1)
#    
#    return NewRaster
    


#DataDirectory = "/run/media/dav/SHETLAND/Analyses/Ryedale_storms_simulation/Gridded/DetachLim/"
#DataDirectory = "/mnt/SCRATCH/Analyses/HydrogeomorphPaper/peak_flood_maps/boscastle/erode_diff/"
DataDirectory = "/mnt/SCRATCH/Analyses/HydrogeomorphPaper/peak_flood_maps/boscastle/erode_diff/test_raster_diff_func/"

filename = DataDirectory + "Elevations0.asc"
drapename = DataDirectory + "WaterDepths2880.asc"

#LSDP.RasterDifference(DataDirectory + "Elevations0.asc", 
#                      DataDirectory + "Elevations4200.asc", 
#                      raster_band=1, 
#                      OutFileName="TestDIFF.asc", 
#                      OutFileType="AAIGrid")


LSDP.MultiDrapeErodeDiffMaps(DataDirectory, "Elevations0.asc", "Ryedale*.bil", 
               "plasma", 
               drape_min_threshold= -4.5,
               drape_max_threshold= -0.05,
               cbar_label = "DEM difference (m)")


# Create the drape array from one of the Catchment model output rasters
#drape_array = LSDP.ReadRasterArrayBlocks(drapename)
# Optional: A lot of the output rasters contain very small values for certain 
# things like water depth or elevation difference, so you can mask this below:
#low_values_index = drape_array < 0.005
#drape_array[low_values_index] = np.nan


"""
LSDP.DrapedOverHillshade(filename,drape_array,clim_val=(0,400), \
                         drape_cmap=trunc_cmap, colorbarlabel='Elevation in meters',\
                         ShowColorbar=True, ShowDrapeColorbar=True,
                         drape_cbarlabel = "Water depth (m)",
                         drape_alpha=1.0)
"""