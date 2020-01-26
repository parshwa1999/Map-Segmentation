import glob
import cv2
import numpy as np
import h5py

print("Start")

data = [cv2.imread(file) for file in glob.glob("clean_roadlabel/*.png")]

print(np.shape(data))

# Write
h5f = h5py.File('clean/clean_roadlabel.h5', 'w')
h5f.create_dataset('clean_roadlabel', data=data)
h5f.close()

"""
# Read
h5f = h5py.File('clean/clean_road.h5','r')
data = h5f['clean_road'][:]
print(data)
h5f.close()
"""