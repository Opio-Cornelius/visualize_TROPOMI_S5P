# -*- coding: utf-8 -*-
"""
Plotting NO2 from OMI and TROPOMI
Created on Fri May 28 12:39:33 2021
@author: opior
"""

# Import the required libararies
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import rasterio as rs


# Read-in the GEOTIFF image
dataset = rs.open('C:/python_work/phd/atm_science/NO2_tropomi_USA.tif')
band_raw = dataset.read(1)

# Convert to molecules/cm**2
band = band_raw * (6.02214e19)

# Define the image extent. These coordinates must be gotten from the google 
#earth engine code
img_extent = (-132.2067654374111, -59.08176543741109, 22.41721803068931, 
              51.38967328104845)


# Set figure parameters
fig = plt.figure(figsize=(8, 4), dpi=500)
mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1

# Plot the map
ax = plt.axes(projection=ccrs.PlateCarree())
plot_no2_tr = ax.imshow(band, cmap='jet', origin='upper', extent=img_extent, 
                  transform=ccrs.PlateCarree(), vmin=1e14, vmax=3.7e15)

# Add geographical features to the map
lakes_10m = cfeature.NaturalEarthFeature('physical','lakes','10m')
states = cfeature.NaturalEarthFeature('cultural', scale="50m",
                             facecolor="none",
                             name="admin_1_states_provinces_lines")
ax.add_feature(lakes_10m, facecolor='none', edgecolor='k')
ax.add_feature(states, linewidth=0.5, edgecolor="black")
ax.coastlines(resolution='10m', color='black', linewidth=0.9)
ax.add_feature(cartopy.feature.BORDERS, linewidth=0.9)
colorbar_axes_tro = plt.gcf().add_axes([0.2, 0.125, 0.6, 0.04])
cb = plt.colorbar(plot_no2_tr, colorbar_axes_tro, 
                  orientation='horizontal', 
                  label='$\mathregular{NO_2}$ (molecules/$\mathregular{cm^2}$)')
plt.show()