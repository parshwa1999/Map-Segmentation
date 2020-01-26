import glob
import cv2
import numpy as np
import h5py

# Write
data = [cv2.imread(file) for file in glob.glob("test/*.png")]

h5f = h5py.File('clean/clean_road.h5', 'w')
h5f.create_dataset('clean_road', data=data)
h5f.close()

"""
# Read
h5f = h5py.File('clean/clean_road.h5','r')
data = h5f['clean_road'][:]
h5f.close()
"""